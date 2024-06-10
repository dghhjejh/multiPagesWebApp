<template>
    <v-container class="leconteneur">
      <v-row>
        <v-col cols="12" md="6" class="mx-auto">
          <v-card class="mb-4">
            <v-card-title>
              <v-text-field v-model="nouvelleTache" label="Titre de la tâche"></v-text-field>
              <v-text-field v-model="description" label="Description"></v-text-field>
              <v-menu
                v-model="showDatePicker"
                transition="scale-transition"
                min-width="auto"
                offset-y
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    :value="selectedDate.toISOString().substring(0, 10)"
                    v-model="showDatePicker"
                    v-bind="attrs"
                    v-on="on"
                    outlined
                    prepend-icon="mdi-calendar"
                    readonly
                    label="Sélectionner une date"
                    @click:prepend="afficherCalendrier"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="selectedDate"
                  @input="showDatePicker = false"
                  no-title
                ></v-date-picker>
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
  
  const showDatePicker = ref(false);
  const nouvelleTache = ref('');
  const description = ref('');
  const taches = ref([]);
  const selectedDate = ref(new Date());
  
  const ajouterTache = () => {
    if (nouvelleTache.value.trim() !== '') {
      taches.value.push({
        tache: nouvelleTache.value,
        date: selectedDate.value.toISOString().substring(0, 10), // Format to string
        description: description.value
      });
      nouvelleTache.value = '';
      description.value = ''; 
    }
  };
  
  const afficherCalendrier = () => {
    showDatePicker.value = true;
  };
  
  const supprimerTache = (indice) => {
    taches.value.splice(indice, 1);
  };
  </script>
  
  <style scoped>
  .leconteneur {
    position: relative;
    top: 110px;
    z-index: 1;
  }
  
  .mx-auto {
    margin-left: auto;
    margin-right: auto;
  }
  
  .v-menu__content {
    z-index: 3000 !important;
  }
  </style>