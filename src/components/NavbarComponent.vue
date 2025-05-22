<template>
  <nav class="navbar" :class="{ 'navbar--open': isOpen }">
    <div class="navbar__container">
      <!-- Logo/Naam aan de linkerkant -->
      <div class="navbar__logo" @click="toggleNavbar">
        <span class="navbar__logo-text">Alperen Ozcelik</span>
        <button class="navbar__toggle" aria-label="Toggle navigation">
          <span class="navbar__toggle-icon" :class="{ 'navbar__toggle-icon--open': isOpen }"></span>
        </button>
      </div>

      <!-- Navigatielinks aan de rechterkant -->
      <div class="navbar__links" :class="{ 'navbar__links--open': isOpen }">
        <router-link
            to="/"
            class="navbar__link"
            active-class="navbar__link--active"
            exact
            @click.native="closeNavbar"
        >
          <span class="navbar__link-text">Startpagina</span>
          <span class="navbar__link-hover"></span>
        </router-link>

        <router-link
            to="/mijn-verhaal"
            class="navbar__link"
            active-class="navbar__link--active"
            @click.native="closeNavbar"
        >
          <span class="navbar__link-text">Mijn Verhaal</span>
          <span class="navbar__link-hover"></span>
        </router-link>

        <router-link
            to="/expertise"
            class="navbar__link"
            active-class="navbar__link--active"
            @click.native="closeNavbar"
        >
          <span class="navbar__link-text">Expertise</span>
          <span class="navbar__link-hover"></span>
        </router-link>

        <router-link
            to="/creaties"
            class="navbar__link"
            active-class="navbar__link--active"
            @click.native="closeNavbar"
        >
          <span class="navbar__link-text">Creaties</span>
          <span class="navbar__link-hover"></span>
        </router-link>

        <router-link
            to="/contact"
            class="navbar__link"
            active-class="navbar__link--active"
            @click.native="closeNavbar"
        >
          <span class="navbar__link-text">Contactinformatie</span>
          <span class="navbar__link-hover"></span>
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      isOpen: false,
      lastScrollPosition: 0
    }
  },
  mounted() {
    window.addEventListener('scroll', this.onScroll)
    window.addEventListener('resize', this.handleResize)
    this.handleResize()
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onScroll)
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    toggleNavbar() {
      this.isOpen = !this.isOpen
    },
    closeNavbar() {
      this.isOpen = false
    },
    onScroll() {
      const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop
      if (currentScrollPosition < 0) return

      // Sluit navbar bij scrollen op mobile
      if (window.innerWidth < 992 && this.isOpen) {
        this.isOpen = false
      }

      this.lastScrollPosition = currentScrollPosition
    },
    handleResize() {
      if (window.innerWidth >= 992) {
        this.isOpen = false
      }
    }
  }
}
</script>

<style scoped>
/* Basisstijlen */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  transition: all 0.3s ease;
}

.navbar__container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 70px;
}

/* Logo stijlen */
.navbar__logo {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.navbar__logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3498db; /* Blauwe kleur */
  transition: color 0.3s;
}

.navbar__logo:hover .navbar__logo-text {
  color: #2980b9; /* Donkerder blauw */
}

/* Toggle knop voor mobile */
.navbar__toggle {
  display: none;
  background: none;
  border: none;
  width: 30px;
  height: 30px;
  position: relative;
  margin-left: 20px;
  cursor: pointer;
}

.navbar__toggle-icon,
.navbar__toggle-icon::before,
.navbar__toggle-icon::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 3px;
  background-color: #3498db; /* Blauwe kleur */
  transition: all 0.3s ease;
}

.navbar__toggle-icon {
  top: 50%;
  transform: translateY(-50%);
}

.navbar__toggle-icon::before {
  top: -8px;
}

.navbar__toggle-icon::after {
  top: 8px;
}

.navbar__toggle-icon--open {
  background-color: transparent;
}

.navbar__toggle-icon--open::before {
  top: 0;
  transform: rotate(45deg);
}

.navbar__toggle-icon--open::after {
  top: 0;
  transform: rotate(-45deg);
}

/* Navigatielinks */
.navbar__links {
  display: flex;
  gap: 20px;
}

.navbar__link {
  position: relative;
  padding: 10px 0;
  color: #2c3e50; /* Donkere tekstkleur */
  text-decoration: none;
  font-weight: 500;
  overflow: hidden;
}

.navbar__link-text {
  position: relative;
  z-index: 1;
  transition: color 0.3s;
}

.navbar__link-hover {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background-color: #2ecc71; /* Groene kleur */
  transform: translateX(-100%);
  transition: transform 0.3s ease;
}

.navbar__link:hover .navbar__link-text {
  color: #3498db; /* Blauwe kleur */
}

.navbar__link:hover .navbar__link-hover {
  transform: translateX(0);
}

.navbar__link--active .navbar__link-text {
  color: #3498db; /* Blauwe kleur */
  font-weight: 600;
}

.navbar__link--active .navbar__link-hover {
  transform: translateX(0);
  background-color: #3498db; /* Blauwe kleur */
}

/* Responsieve stijlen */
@media (max-width: 991px) {
  .navbar__toggle {
    display: block;
  }

  .navbar__links {
    position: fixed;
    top: 70px;
    left: 0;
    right: 0;
    background-color: white;
    flex-direction: column;
    align-items: center;
    padding: 20px 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transform: translateY(-100%);
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
  }

  .navbar__links--open {
    transform: translateY(0);
    opacity: 1;
    pointer-events: all;
  }

  .navbar__link {
    padding: 15px 0;
    font-size: 1.1rem;
  }
}
</style>
