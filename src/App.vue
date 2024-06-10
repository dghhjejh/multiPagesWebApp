<template>
  <div id="app">
    <header>
      <NavBar/>
    </header>
    <router-view/>
  </div>
</template>

<script setup>
import NavBar from './components/NavBar.vue';

</script>
<style>
nav {
  padding: 15px;
}
nav a {
  margin: 0 15px;
}
</style>