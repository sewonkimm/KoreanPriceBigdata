<template>
  <div class="login">
    <!-- 로고 -->
    <div class="logo">
      <LogoName />
    </div>

    <!-- 로그인 폼 -->
    <LoginForm />

    <!-- 소셜 로그인 모달 -->
    <v-dialog v-model="dialog" width="320">
      <template v-slot:activator="{ on, attrs }">
        <div class="button">
          <v-btn class="socialLoginButton" dark v-bind="attrs" v-on="on">
            다른 방법으로 시작하기
          </v-btn>
        </div>
      </template>

      <v-card>
        <v-card-title color="#608F58" class="informationMessage">
          다른 방법으로 시작하기
        </v-card-title>

        <div class="socialLoginLogo"><Google /></div>
        <div class="socialLoginLogo"><Kakao /></div>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="#608F58" text @click="dialog = false">
            닫기
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <router-link to="Register" class="registerButton">회원가입</router-link>
  </div>
</template>

<script>
import '@/components/css/login/style.scss';
import LoginForm from '@/components/login/loginForm';
import { LogoName, Google, Kakao } from '@/assets/index.js';

export default {
  name: 'Login',
  components: {
    LoginForm,
    LogoName,
    Google,
    Kakao,
  },
  data() {
    return {
      dialog: false,
    };
  },
};
</script>
