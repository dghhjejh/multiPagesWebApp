
<template>
    <div class="barre_de_recherche">
        <input type="text" placeholder="nom du pays" :value="modelValue" @input="handleInput" class="entree"/>
        <ul class="options" v-show="resultatsDeRecherche.length && isOpen">
            <li class="uneOption" v-for="resultat in resultatsDeRecherche" :key="resultat.nom" @click="setSelected(resultat.nom)">
                {{ resultat.nom }}
            </li>
        </ul>
    </div>
 </template>
 
 <script setup>
/* eslint-disable */
import {computed, ref} from 'vue';
const props = defineProps({
    source:{
        type: Array,
        required:true,
        default: () => []

    },
    modelValue: String
})

const emit = defineEmits(["update:modelValue"])
const recherche = ref("")


const resultatsDeRecherche = computed(()=>{
    if(recherche.value ==""){
        return []
    }

    return props.source.filter(item=>{
        if(item.nom.toLowerCase().includes(recherche.value.toLowerCase())){
            return item
        }
    })
})

const isOpen = ref(false)

const setSelected = item => {
    isOpen.value = false
    recherche.value = item
    emit("update:modelValue", recherche.value)
}
const handleInput = event =>{
    isOpen.value = true
    recherche.value = event.target.value
    emit("update:modelValue", recherche.value)
}
 </script>

<style>
.barre_de_recherche {
    position: relative;
    width:100%;
}
.entree{
    width: 100%;
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
    border-width: 1px;
    border-style: solid;
    border-color: #d1d5db;
    border-radius: 0.25rem;
    font-size: 1rem;
    padding-left: 1.25rem;
    padding-right: 1.25rem;
}
.options{
    margin-top: 0.25rem;
    width: 100%;
    max-height: 15rem;
    border-width: 1px;
    border-style: solid;
    border-color: #d1d5db;
    border-radius: 0.375rem;
    background-color: #fff;
    position: absolute;
    overflow-y: auto;
}
.uneOption {
  padding-left: 1rem;
  padding-right: 1rem;
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: #e2e8f0;
  color: #4a5568;
  cursor: pointer;
}

.uneOption:hover {
  background-color: #f7fafc;
  transition-property: background-color;
  transition-duration: 0.3s;
}
</style>
 