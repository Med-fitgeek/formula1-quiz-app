<template>
  <div>
    <h2>{{ currentQuestion.text }}</h2>
    <img
      v-if="currentQuestion.image"
      :src="currentQuestion.image"
      alt="Question Image"
    />
    <ul>
      <li
        v-for="(answer, index) in currentQuestion.answers"
        :key="index"
        @click="emit('answer-selected', index)"
      >
        {{ answer }}
      </li>
    </ul>
  </div>
</template>

<script setup>
const props = defineProps({
  currentQuestion: Object,
});

const emit = defineEmits(['answer-selected']);
</script>
