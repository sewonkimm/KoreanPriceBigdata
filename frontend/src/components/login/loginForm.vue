<template>
  <div class="loginForm">
    <v-form class="input">
      <v-container>
        <v-row>
          <v-text-field v-model="email" label="이메일" required></v-text-field>
        </v-row>
        <v-row>
          <v-text-field
            v-model="password"
            label="비밀번호"
            required
            counter
            :append-icon="showText ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showText ? 'text' : 'password'"
            @click:append="showText = !showText"
          ></v-text-field>
        </v-row>
      </v-container>
    </v-form>

    <v-btn :class="{ active: isActive, loginButton: 'loginButton' }" height="63" @click="login"
      >로그인</v-btn
    >
  </div>
</template>
<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      email: '',
      password: '',
      showText: false, // 비밀번호 보여줄지 말지 결정
      isActive: false, // 로그인 버튼 활성화 비활성화 결정
    };
  },
  watch: {
    // email과 password값이 바뀔때마다 함수 실행
    email: function() {
      this.buttonActive();
    },
    password: function() {
      this.buttonActive();
    },
  },
  methods: {
    buttonActive: function() {
      // email과 password를 모두 입력했을 때 로그인 버튼 활성화
      if (this.email !== '' && this.password !== '') {
        this.isActive = true;
      } else this.isActive = false;
    },
    login: function() {
      this.$axios({
        url: '/members/login',
        method: 'POST',
        data: {
          memberEmail: this.email,
          memberPassword: this.password,
          memberGender: '',
          memberArea: '',
          memberBirth: '',
          memberName: '',
          memberPlatformType: '',
        },
      })
        .then(() => {
          this.$router.push({ name: 'Main' });
        })
        .catch((error) => {
          console.error(error);
          alert('이메일과 비밀번호를 확인해주세요.');
        });
    },
  },
};
</script>
