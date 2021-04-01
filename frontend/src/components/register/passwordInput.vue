<template>
  <div class="passwordInput">
    <div class="informationMessage">
      <h1>비밀번호를 입력해주세요.</h1>
    </div>
    <v-form>
      <v-container fluid>
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
        <v-row>
          <v-text-field
            v-model="passwordRe"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min, passwordConfirmationRule]"
            :type="show ? 'text' : 'password'"
            name="input-10-1"
            label="비밀번호 확인"
            hint="At least 8 characters"
            counter
            @click:append="show = !show"
          ></v-text-field>
        </v-row>
      </v-container>
    </v-form>
    <button class="nextButton" v-on:click="nextButton">
      <router-link to="/login" class="registerButton">회원가입</router-link>
    </button>
  </div>
</template>
<script>
import '@/components/css/register/style.scss';

export default {
  name: 'PasswordInput',
  components: {},
  methods: {
    nextButton: function(event) {
      alert('회원가입 완료! 메인 페이지로 이동합니다 :)');
    },
  },
  data() {
    return {
      show1: true,
      email: '',
      password: '',
      passwordRe: '',
      rules: {
        required: (value) => !!value || '필수로 입력해야 합니다..',
        min: (v) => v.length >= 8 || '비밀번호는 최소 8글자입니다.',
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || '이메일 형식에 맞춰 작성해주세요.';
        },
      },
    };
  },
  computed: {
    passwordConfirmationRule() {
      return () => this.password === this.passwordRe || '비밀번호는 동일해야 합니다';
    },
  },
};
</script>
