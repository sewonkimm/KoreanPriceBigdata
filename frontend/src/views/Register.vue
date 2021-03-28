<template>
  <h1>
    회원가입 페이지 입니다.
  </h1>
</template>
<script>
import '@/components/css/main/style.scss';

export default {
  name: 'Register',
  components: {},
  data: () => ({
    email: '',
    password: '',
  }),
};
</script>
