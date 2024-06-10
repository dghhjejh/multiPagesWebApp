<template>
    <v-container class="leconteneur">
      <v-row>
        <v-col cols="12" md="6" class="mx-auto">
          <v-card class="mb-4">
            <v-card-title>
              <v-text-field v-model="nouvelleTache" label="Titre de la tâche"></v-text-field>
              <v-text-field v-model="description" label="Description"></v-text-field>
              <v-text-field v-model="selectedDate" label="Sélectionner une date" outlined prepend-icon="mdi-calendar" @click:append="afficherCalendrier" readonly></v-text-field>
              <v-menu
              v-model="showDatePicker"
              :close-on-content-click="false"
              transition="scale-transition"
              min-width="auto"
              offset-y
              >
                <v-date-picker
                 v-model="selectedDate"
                @input="showDatePicker = false"
                >
                </v-date-picker>
              </v-menu>
            </v-card-title>
            <v-card-actions>
              <v-btn icon @click="ajouterTache">
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
  
        <v-col cols="12" md="6" class="mx-auto">
          <v-card
            v-for="(item, indice) in taches"
            :key="indice"
            class="mb-4"
          >
            <v-card-title>
              <div>Titre: {{ item.tache }}</div>
              <div>Description: {{ item.description }}</div>
              <div>Date: {{ item.date }}</div>
              <v-spacer></v-spacer>
              <v-btn icon @click="supprimerTache(indice)">
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const getLocalDateString = () => {
    const date = new Date();
    date.setMinutes(date.getMinutes() - date.getTimezoneOffset());
    return date.toISOString().substring(0, 10);
  };
  const showDatePicker = ref(false);
  const nouvelleTache = ref('');
  const description = ref('');
  const taches = ref([]);
  const selectedDate = ref(getLocalDateString());
  const ajouterTache = () => {
    if (nouvelleTache.value.trim() !== '') {
      taches.value.push({
        tache: nouvelleTache.value,
        date: selectedDate.value,
        description: description.value
      });
      nouvelleTache.value = '';
      description.value = ''; 
    }
  };
  const afficherCalendrier = () => {
    showDatePicker.value = true;
  } 
  const supprimerTache = (indice) => {
    taches.value.splice(indice, 1);
  };
  </script>
  
  <style scoped>
  .leconteneur {
    position: relative;
    top: 110px;
    z-index: 9999;
  }
  
  .mx-auto {
    margin-left: auto;
    margin-right: auto;
  }
  </style>