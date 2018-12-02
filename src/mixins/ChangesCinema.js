export default {
  methods: {
    cinemas () {
      return this.$store.getters['getCinemas']
    },
    setCinemaCookie () {
      this.$cookie.set('cinema', this.currentCinema)
    }
  },
  computed: {
    currentCinema: {
      get () {
        return this.$store.getters['getCurrentCinema']
      },
      set (newValue) {
        this.$store.dispatch('setCurrentCinema', newValue)
      }
    }
  }
}