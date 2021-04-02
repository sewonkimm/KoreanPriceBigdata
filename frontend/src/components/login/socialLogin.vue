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
          this.id = result.user.email;
          this.$axios({
            url: '/members/social',
            method: 'POST',
            data: {
              memberEmail: result.user.email,
              memberPassword: null,
              memberName: result.user.displayName,
              memberPlatformType: 'Google',
            },
          })
            .then((response) => {
              if (response.data.message === 'Success') {
                const token = response.data.accesstoken;
                localStorage.setItem('accesstoken', token);
                this.$store.commit('setId', this.id);
                alert('구글 로그인에 성공하셨습니다.');
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
          let gender = '';
          if (kakaoAccount.gender === 'female') {
            gender = 'F';
          } else if (kakaoAccount.gender === 'male') {
            gender = 'M';
          } else {
            gender = null;
          }
          if (kakaoAccount.email === null) {
            // kakao 전용 회원가입 필요
          } else {
            this.$axios({
              url: '/members/social',
              method: 'POST',
              data: {
                memberEmail: kakaoAccount.email,
                memberPassword: null,
                memberName: kakaoAccount.profile.nickname,
                memberGender: gender,
                memberBirth: kakaoAccount.birthday,
                memberPlatformType: 'Kakao',
              },
            })
              .then((response) => {
                if (response.data.message === 'Success') {
                  const token = response.data.accesstoken;
                  localStorage.setItem('accesstoken', token);
                  this.$store.commit('setId', this.id);
                  alert('카카오 로그인에 성공하셨습니다.');
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
