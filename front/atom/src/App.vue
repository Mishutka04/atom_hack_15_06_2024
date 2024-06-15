<script setup>

import { useRouter } from "vue-router";
const router = useRouter();

const Item_get = (id) => {
  router.push('/route/' + id);
}

</script>

<template>

<router-view :key='$route.fullPath'></router-view>

</template>

<style>
</style>
