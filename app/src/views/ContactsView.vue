<template>
  <c-circular-progress :value="80" v-if="loading" is-indeterminate />

  <c-flex
    align="center"
    border="1px solid"
    direction="column"
    width="50%"
    v-else
  >
    <c-flex borderBottom="1px solid" w="100%" justifyContent="center"
      >Lista de Contatos</c-flex
    >
    <c-flex width="100%" justify="flex-start" borderBottom="1px solid">
      <c-flex w="50%" alignItems="center" justifyContent="center">
        Domínio
      </c-flex>
      <c-flex
        w="50%"
        direction="column"
        borderLeft="1px solid"
        alignItems="center"
        justifyItems="center"
      >
        Contato
      </c-flex>
    </c-flex>
    <c-flex
      width="100%"
      justify="flex-start"
      borderBottom="1px solid"
      v-for="(group, index) in conectionsData"
      :key="index"
    >
      <c-flex w="50%" alignItems="center" justifyContent="center">
        {{ group.domain }}
      </c-flex>
      <c-flex
        w="50%"
        direction="column"
        borderLeft="1px solid"
        alignItems="center"
        justifyItems="center"
      >
        <span v-for="(email, j) in group.emails" :key="j">{{ email }}</span>
      </c-flex>
    </c-flex>
  </c-flex>
</template>

<script lang="ts">
import { api } from '../api'
import {
  CCircularProgress,
  CCircularProgressLabel,
  CFlex
} from '@chakra-ui/vue'

interface IConection {
  emailAddresses: {
    value: string
    metadata: {
      primay: boolean
      spurce: {
        id: string
        type: string
      }
    }
    etag: string
  }[]
  names: {
    displayName: string
    displayNameLastFirst: string
    familyName: string
    givenName: string
    unstructuredName: string
  }[]
}

export default {
  data() {
    return {
      code: null as string | null,
      loading: false,
      connections: [] as IConection[],
      conectionsData: [] as { domain: string; emails: string[] }[]
    }
  },
  created() {
    this.code = this.$route.query.code as string | null
    if (this.code) {
      this.handleAuthCode(this.code)
    }
  },
  watch: {
    connections(newConections: IConection[]) {
      console.log(newConections)
      this.generateDataFromConections(newConections)
    }
  },
  components: {
    CCircularProgress,
    CCircularProgressLabel,
    CFlex
  },
  methods: {
    async handleAuthCode(code: string) {
      this.loading = true
      try {
        const tokenResponse = await api.post(
          '/api/generatetoken',
          JSON.stringify({ code }),
          {
            headers: { 'Content-Type': 'application/json' }
          }
        )
        const token = JSON.parse(tokenResponse.data).token

        if (!token) throw new Error('Token não foi gerado.')

        const contactsResponse = await api.post(
          '/api/contacts',
          JSON.stringify({ google_token: token }),
          {
            headers: { 'Content-Type': 'application/json' }
          }
        )
        console.log(contactsResponse.data)
        this.$data.connections = JSON.parse(contactsResponse.data).connections
      } catch (error) {
        console.error('Erro ao processar requisição:', error)
      } finally {
        this.loading = false
      }
    },
    generateDataFromConections(conections: IConection[]) {
      console.log(conections)
      if (conections && conections.length > 0) {
        conections.forEach((conection) => {
          const emails = conection.emailAddresses.map(
            (emailData) => emailData.value
          )
          const domains = Array.from(
            new Set(
              emails.map((email) => {
                return email.match(/(@.*)/)![1]
              })
            )
          )

          domains.forEach((domain) => {
            const dataIndex = this.$data.conectionsData.findIndex(
              (data) => data.domain === domain
            )
            if (dataIndex === -1) {
              const newItem = {
                domain,
                emails: emails.filter((email) => email.includes(domain))
              }
              this.$data.conectionsData.push(newItem)
            } else {
              this.$data.conectionsData[dataIndex].emails.push(
                ...emails.filter((email) => email.includes(domain))
              )
            }
          })
        })
      }
    }
  }
}
</script>

<style scoped></style>
