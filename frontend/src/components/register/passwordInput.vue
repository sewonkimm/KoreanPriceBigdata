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
            :rules="alphabetRules"
            :type="show ? 'text' : 'password'"
            label="비밀번호"
            counter
            required
            @click:append="show = !show"
          ></v-text-field>
        </v-row>
        <v-row>
          <v-text-field
            v-model="passwordConfirm"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="passwordConfirmationRule"
            :type="show ? 'text' : 'password'"
            label="비밀번호 확인"
            counter
            required
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
      if (this.password !== '') {
        this.isActive = true;
      } else this.isActive = false;
    },
  },
  data() {
    return {
      isActive: false, // 회원가입 버튼 활성화 비활성화 결정
      show: false,
      password: '',
      passwordConfirm: '',
      alphabetRules: [
        (value) =>
          /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$/.test(value) ||
          '소문자와 대문자, 숫자를 모두 포함하고 8자 이상이어야 합니다.',
      ],
    };
  },
  watch: {
    // password값이 바뀔때마다 함수 실행
    password: function() {
      this.buttonActive();
    },
  },
  computed: {
    passwordConfirmationRule() {
      return () => this.password === this.passwordConfirm || '비밀번호는 동일해야 합니다';
    },
  },
};
</script>
