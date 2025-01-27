export interface IConection {
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
