<template>
  <div class="socialLogin">
    <v-dialog v-model="dialog" width="320">
      <template v-slot:activator="{ on, attrs }">
        <v-btn class="socialLoginButton" height="63" v-bind="attrs" v-on="on">
          다른 방법으로 시작하기
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="title">
          다른 방법으로 시작하기
        </v-card-title>

        <div class="socialLoginButton">
          <Google @click="loginWithGoogle" />
          <Kakao @click="loginWithKakao" />
        </div>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="dialog = false" class="closeButton">
            닫기
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import { Google, Kakao } from '@/assets/index.js';
import firebase from 'firebase';
import '@firebase/auth';
import '@firebase/firestore';

export default {
  name: 'SocialLogin',
  components: {
    Google,
    Kakao,
  },
  data() {
    return {
      dialog: false,
      id: '',
    };
  },
  methods: {
    loginWithGoogle: function() {
      const provider = new firebase.auth.GoogleAuthProvider();
      firebase.auth().languageCode = 'ko';
      firebase
        .auth()
        .signInWithPopup(provider)
        .then((result) => {
          const googleFormData = new FormData();
          this.id = result.user.email;
          googleFormData.append('memberEmail', result.user.email);
          googleFormData.append('memberPassword', null);
          googleFormData.append('memberName', result.user.displayName);
          googleFormData.append('memberPlatformType', 'Google');
          this.$axios({
            url: '/member/social',
            method: 'POST',
            data: googleFormData,
          })
            .then((response) => {
              if (response.data.message === 'success') {
                const token = response.data((accesstoken) => {
                  return accesstoken;
                });
                localStorage.setItem('accesstoken', token);
                this.$store.commit('setId', id);
              } else {
                alert('구글 로그인에 실패했습니다.');
              }
            })
            .catch((error) => {
              console.error(error);
            });
        });
    },
    loginWithKakao: function() {
      window.Kakao.Auth.login({
        scope: 'profile, age_range, account_email, gender, birthday',
        success: this.getInfoWithKaKao,
      });
    },
    getInfoWithKaKao: function() {
      window.Kakao.API.request({
        url: '/v2/user/me',
        success: async (res) => {
          const kakaoAccount = res.kakao_account;
          if (info.memberEmail === null) {
            // kakao 전용 회원가입 필요
          } else {
            const kakaoFormData = new FormData();
            kakaoFormData.append('memberEmail', kakao.email);
            kakaoFormData.append('memberPassword', null);
            kakaoFormData.append('memberName', kakaoAccount.profile.nickname);
            kakaoFormData.append('memberGender', kakaoAccount.gender);
            kakaoFormData.append('memberBirth', kakaoAccount.birthday);
            kakaoFormData.append('memberPlatformType', 'Kakao');
            this.$axios({
              url: '/member/social',
              method: 'POST',
              data: kakaoFormData,
            })
              .then((response) => {
                if (response.data.message === 'success') {
                  const token = response.data((accesstoken) => {
                    return accesstoken;
                  });
                  localStorage.setItem('accesstoken', token);
                  this.$store.commit('setId', id);
                } else {
                  alert('카카오 로그인에 실패했습니다.');
                }
              })
              .catch((error) => {
                console.error(error);
              });
          }
        },
      });
    },
  },
};
</script>
