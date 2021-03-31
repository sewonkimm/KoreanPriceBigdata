<template>
  <div class="emailInput">
    <div class="informationMessage">
      <h1>이메일을 입력해주세요</h1>
    </div>
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
      </v-container>
    </v-form>
    <!-- <button class="nextButton" v-on:click="nextButton">
      다음
    </button> -->
  </div>
</template>
<script>
import '@/components/css/register/style.scss';

export default {
  name: 'EmailInput',
  components: {},
  methods: {
    nextButton: function(event) {
      alert('다음 버튼 클릭');
    },
  },
  data() {
    return {
      show1: true,
      email: '',
      rules: {
        required: (value) => !!value || '필수로 입력해야 합니다..',
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || '이메일 형식에 맞춰 작성해주세요.';
        },
      },
    };
  },
};
</script>
