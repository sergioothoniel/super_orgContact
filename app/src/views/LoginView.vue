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

    <c-button
      w="60%"
      alignSelf="center"
      variant-color="blue"
      variant="outline"
      @click="getGoogleAuthURL"
    >
      Entrar com conta Google
    </c-button>
  </c-flex>
</template>

<script setup lang="ts">
import { api } from '../api'
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
import { onMounted } from 'vue'

defineProps<{}>()

const getGoogleAuthURL = async () => {
  api
    .get('/api/auth-url')
    .then((res) => {
      const authUrl = JSON.parse(res.data).auth_url
      if (!authUrl) console.error('Não foi possível recuperar URL:', res.data)
      window.location = authUrl
    })
    .catch((err) => console.error(err))
}
</script>
