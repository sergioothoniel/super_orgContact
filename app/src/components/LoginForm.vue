<template>
  <c-flex
    w="45%"
    h="50vh"
    borderWidth="1px"
    borderRadius="lg"
    p="4"
    flexDirection="column"
    alignItems="center"
    justifyContent="center"
  >
    <c-heading as="h1" size="2xl" margin="0 0 20px 0">
      Super OrgContact
    </c-heading>
    <c-form-control
      w="95%"
      h="60%"
      display="flex"
      flexDirection="column"
      justifyContent="space-around"
    >
      <c-form-label for="email">Email Google</c-form-label>
      <c-input type="email" id="email" />

      <c-form-label for="password">Senha</c-form-label>
      <c-input type="password" id="password" />
      <c-button
        w="60%"
        alignSelf="center"
        variant-color="blue"
        variant="outline"
      >
        Button
      </c-button>
    </c-form-control>
  </c-flex>
</template>

<script setup lang="ts">
import {
  CBox,
  CFormControl,
  CFormLabel,
  CFormErrorMessage,
  CFormHelperText,
  CInput,
  CFlex,
  CButton,
  CHeading
} from '@chakra-ui/vue'

defineProps<{}>()
</script>
