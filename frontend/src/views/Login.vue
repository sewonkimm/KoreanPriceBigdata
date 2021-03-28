<template>
  <div class="login">
    <!-- 로고 -->
    <div class="logo">
      <Logo />
    </div>

    <v-form>
      <v-container fluid>
        <v-row>
          <v-text-field
            v-model="email"
            :rules="[rules.required, rules.email]"
            name="input-10-1"
            label="이메일"
            outlined
          ></v-text-field>
        </v-row>
        <v-row>
          <v-text-field
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="비밀번호"
            hint="At least 8 characters"
            counter
            @click:append="show1 = !show1"
            outlined
          ></v-text-field>
        </v-row>
      </v-container>
    </v-form>
    <button type="submit" class="loginButton">로그인</button>
    <button type="submit" class="socialLoginButton">
      다른 방법으로 시작하기
    </button>

    <router-link to="Register">회원가입</router-link>
  </div>
</template>
<script>
import '@/components/css/main/style.scss';
import { Logo } from '@/assets/index.js';

export default {
  name: 'Login',
  components: {
    Logo,
  },
  data() {
    return {
      show1: true,
      email: '',
      password: '',
      rules: {
        required: (value) => !!value || 'Required.',
        min: (v) => v.length >= 8 || 'Min 8 characters',
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || 'Invalid e-mail.';
        },
      },
    };
  },
  methods: {},
};
</script>
