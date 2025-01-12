<script setup>
import { ref } from "vue";

// Événement émis au parent
const emit = defineEmits(["file-change"]);

// Références
const fileReader = new FileReader();
const fileInput = ref(null);
const fileDataUrl = ref("");
const isSaving = ref(false);

// Validation et encodage de l'image
function fileChange(event) {
  const file = event.target.files[0];

  // Validation : taille max 2 Mo
  if (file.size > 2 * 1024 * 1024) {
    alert("L'image sélectionnée est trop volumineuse. Maximum : 2 Mo.");
    return;
  }

  // Validation : types autorisés
  const allowedTypes = ["image/jpeg", "image/png", "image/gif"];
  if (!allowedTypes.includes(file.type)) {
    alert("Seules les images JPEG, PNG ou GIF sont autorisées.");
    return;
  }

  // Lire le fichier en base64
  isSaving.value = true;
  fileReader.onload = () => {
    fileDataUrl.value = fileReader.result;
    emit("file-change", fileDataUrl.value); // Émettre au parent
    isSaving.value = false;
  };
  fileReader.readAsDataURL(file);
}

// Supprimer l'image
function removeImage() {
  fileDataUrl.value = "";
  emit("file-change", ""); // Émettre une valeur vide au parent
  if (fileInput.value) fileInput.value.value = ""; // Réinitialiser l'input
}
</script>

<template>
  <div>
    <!-- Input pour télécharger une image -->
    <input
      type="file"
      accept="image/jpeg, image/png, image/gif"
      @change="fileChange"
      ref="fileInput"
      :disabled="isSaving"
      class="input-file"
    />

    <!-- Prévisualisation de l'image -->
    <img
      v-if="fileDataUrl"
      :src="fileDataUrl"
      alt="Prévisualisation"
      class="preview"
    />

    <!-- Bouton pour supprimer l'image -->
    <button
      v-if="fileDataUrl"
      @click="removeImage"
      class="remove-btn"
    >
      Supprimer l'image
    </button>
  </div>
</template>

<style scoped>
.input-file {
  margin: 10px 0;
  display: block;
}

.preview {
  display: block;
  margin-top: 10px;
  max-width: 200px;
  max-height: 200px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.remove-btn {
  margin-top: 10px;
  background-color: red;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}

.remove-btn:hover {
  background-color: darkred;
}
</style>
