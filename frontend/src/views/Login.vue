<template>
  <div class="login">
    <!-- 로고 -->
    <div class="logo">
      <LogoName />
    </div>

    <!-- 로그인 폼 -->
    <v-form>
      <v-container fluid>
        <v-row>
          <v-text-field
            v-model="email"
            :rules="[rules.required, rules.email]"
            name="input-10-1"
            label="이메일"
          ></v-text-field>
        </v-row>
        <v-row>
          <v-text-field
            v-model="password"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show ? 'text' : 'password'"
            name="input-10-1"
            label="비밀번호"
            hint="At least 8 characters"
            counter
            @click:append="show = !show"
          ></v-text-field>
        </v-row>
      </v-container>
    </v-form>
    <div class="button">
      <v-btn class="loginButton">로그인</v-btn>
    </div>

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

    <router-link to="Register" class="register">회원가입</router-link>
  </div>
</template>

<script>
import '@/components/css/main/style.scss';
import { LogoName, Google, Kakao } from '@/assets/index.js';

export default {
  name: 'Login',
  components: {
    LogoName,
    Google,
    Kakao,
  },
  data() {
    return {
      isModalViewed: false,
      show: true,
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
  computed: {
    btndisable: function() {
      return !email || !password;
    },
  },
  methods: {},
};
</script>
