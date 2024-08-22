<template>
    <div id="app">
        <circles-to-rhombuses-spinner
  :animation-duration="1200"
  :circles-num="3"
  :circle-size="15"
  color="#ff1d5e"
/>
    </div>
  </template>
  
  <script setup>
  import { CirclesToRhombusesSpinner } from 'epic-spinners';
  </script>