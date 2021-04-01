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
            :rules="[rules.required, rules.alphabet]"
            :type="show ? 'text' : 'password'"
            label="비밀번호"
            counter
            @click:append="show = !show"
          ></v-text-field>
        </v-row>
        <v-row>
          <v-text-field
            v-model="passwordRe"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, passwordConfirmationRule]"
            :type="show ? 'text' : 'password'"
            label="비밀번호 확인"
            counter
            @click:append="show = !show"
          ></v-text-field>
        </v-row>
      </v-container>
    </v-form>
    <v-btn
      @click="nextButton()"
      :class="{ active: isActive, registerButton: 'registerButton' }"
      height="63"
      >회원가입</v-btn
    >
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
      this.$router.push('/');
    },
    buttonActive: function() {
      // email과 password를 모두 입력했을 때 로그인 버튼 활성화
      if (this.password !== '') {
        this.isActive = true;
      } else this.isActive = false;
    },
  },
  data() {
    return {
      isActive: false, // 회원가입 버튼 활성화 비활성화 결정
      show: false,
      email: '',
      password: '',
      passwordRe: '',
      rules: {
        required: (value) => !!value || '필수로 입력해야 합니다..',
        alphabet: (v) => {
          const pattern = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$/;
          return pattern.test(v) || '소문자와 대문자, 숫자를 모두 포함하고 8자 이상이어야 합니다.';
        },
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || '이메일 형식에 맞춰 작성해주세요.';
        },
      },
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
  computed: {
    passwordConfirmationRule() {
      return () => this.password === this.passwordRe || '비밀번호는 동일해야 합니다';
    },
  },
};
</script>
