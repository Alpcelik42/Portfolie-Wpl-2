<template>
  <div class="home-view">
    <!-- Hero Sectie -->
    <section class="hero-section">
      <div class="container">
        <div class="hero-content">
          <div class="text-content" ref="textContent">
            <h1 class="welcome-text">Welkom!</h1>
            <p class="intro-text">
              Ik ben Alperen Ozcelik, een professionele Web Developer met een passie voor het creëren van uitzonderlijke websites die opvallen.
            </p>
            <button @click="navigateTo('story')" class="story-button">
              Mijn Verhaal
              <span class="button-arrow">→</span>
            </button>
          </div>
          <div class="image-circle" ref="imageCircle">
            <img src="@/assets/images/1000112012025.png" alt="Alperen Ozcelik" class="profile-image" />
          </div>
        </div>
      </div>
    </section>

    <!-- Over Mij Sectie -->
    <section class="about-section" ref="aboutSection">
      <div class="container">
        <h2 class="section-title">Over Mij</h2>
        <div class="about-content">
          <p class="about-text">
            Hallo, mijn naam is Alperen Ozcelik en ik ben 22 jaar oud. Ik ben een enthousiaste en gepassioneerde webontwikkelaar met jaren ervaring in het creëren van websites die zowel functioneel als visueel aantrekkelijk zijn. Wat mij onderscheidt, is mijn oog voor detail en mijn vermogen om technische perfectie te combineren met een uniek design. Ik streef ernaar om elke website tot leven te brengen met innovatieve oplossingen en een gebruiksvriendelijke ervaring. Mijn doel is om digitale projecten te maken die indruk maken en waarde toevoegen.
          </p>
        </div>
      </div>
    </section>

    <!-- Expertise Sectie -->
    <section class="expertise-section" ref="expertiseSection">
      <div class="container">
        <h2 class="section-title">Mijn Expertise</h2>
        <div class="expertise-grid">
          <div
            v-for="(expertise, index) in expertises"
            :key="index"
            class="expertise-item"
            @mouseenter="hoverExpertise(index)"
            @mouseleave="resetExpertise"
          >
            <div class="expertise-icon" :style="{ backgroundColor: expertise.color }">
              {{ expertise.emoji }}
            </div>
            <h3>{{ expertise.title }}</h3>
          </div>
        </div>
      </div>
    </section>

    <!-- Creaties Sectie -->
    <section class="creations-section" ref="creationsSection">
      <div class="container">
        <h2 class="section-title">Mijn Creaties</h2>
        <p class="creations-intro">Hier zijn enkele van mijn recente projecten:</p>
        <div class="projects-grid">
          <div
            v-for="(project, index) in projects"
            :key="index"
            class="project-card"
            @click="navigateTo('creations')"
            @mouseenter="hoverProject(index)"
            @mouseleave="resetProject"
            :style="{ '--hover-color': project.color }"
          >
            <h3>{{ project.name }}</h3>
            <p class="project-description">{{ project.description }}</p>
            <div class="project-link">Bekijk project →</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Floating decoratie elementen -->
    <div class="floating-elements">
      <div class="floating-circle circle-1"></div>
      <div class="floating-circle circle-2"></div>
      <div class="floating-circle circle-3"></div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

export default {
  name: 'HomeView',
  setup() {
    const router = useRouter()
    const textContent = ref(null)
    const imageCircle = ref(null)
    const aboutSection = ref(null)
    const expertiseSection = ref(null)
    const creationsSection = ref(null)

    const expertises = ref([
      { title: 'Web Design', emoji: '🎨', color: '#FF9E9E' },
      { title: 'Frontend Development', emoji: '💻', color: '#A0E7E5' },
      { title: 'Responsieve Websites', emoji: '📱', color: '#B5EAEA' },
      { title: 'UI/UX Design', emoji: '✨', color: '#FFD3B6' }
    ])

    const projects = ref([
      { name: 'Project 1: Plantsome', description: 'Een planten webshop met geavanceerde filters', color: '#8FD3E8' },
      { name: 'Project 2: GroenteWinkel', description: 'Online groentewinkel met bezorgservice', color: '#A8E6CF' },
      { name: 'Project 3: FlightManager', description: 'Vluchtbeheersysteem voor reisbureaus', color: '#FFAAA5' },
      { name: 'Project 4: Cisco Packet tracer', description: 'Netwerk simulatie tool', color: '#FF8B94' },
      { name: 'Project 5: Kassasysteem voor Mosselfestijn', description: 'Custom kassa oplossing voor evenement', color: '#DCEDC1' }
    ])

    const navigateTo = (route) => {
      gsap.to('.home-view', {
        opacity: 0,
        duration: 0.3,
        onComplete: () => router.push({ name: route })
      })
    }

    const hoverExpertise = (index) => {
      gsap.to(`.expertise-item:nth-child(${index + 1}) .expertise-icon`, {
        scale: 1.1,
        rotation: 10,
        duration: 0.3
      })
      gsap.to(`.expertise-item:nth-child(${index + 1}) h3`, {
        color: expertises.value[index].color,
        duration: 0.3
      })
    }

    const resetExpertise = () => {
      gsap.to('.expertise-icon', {
        scale: 1,
        rotation: 0,
        duration: 0.3
      })
      gsap.to('.expertise-item h3', {
        color: '#333',
        duration: 0.3
      })
    }

    const hoverProject = (index) => {
      gsap.to(`.project-card:nth-child(${index + 1})`, {
        y: -10,
        boxShadow: `0 15px 30px -5px ${projects.value[index].color}80`,
        duration: 0.3
      })
    }

    const resetProject = () => {
      gsap.to('.project-card', {
        y: 0,
        boxShadow: '0 5px 15px rgba(0,0,0,0.1)',
        duration: 0.3
      })
    }

    onMounted(() => {
      // Hero section animatie
      gsap.from(textContent.value.children, {
        opacity: 0,
        y: 20,
        duration: 0.8,
        stagger: 0.2,
        ease: 'power2.out'
      })

      gsap.from(imageCircle.value, {
        opacity: 0,
        scale: 0.5,
        duration: 1,
        ease: 'elastic.out(1, 0.5)'
      })

      // Scroll animaties
      gsap.from(aboutSection.value, {
        opacity: 0,
        y: 50,
        duration: 0.8,
        scrollTrigger: {
          trigger: aboutSection.value,
          start: 'top 80%',
          toggleActions: 'play none none none'
        }
      })

      gsap.from(expertiseSection.value.children, {
        opacity: 0,
        y: 50,
        duration: 0.6,
        stagger: 0.1,
        scrollTrigger: {
          trigger: expertiseSection.value,
          start: 'top 80%',
          toggleActions: 'play none none none'
        }
      })

      gsap.from(creationsSection.value.children, {
        opacity: 0,
        y: 50,
        duration: 0.6,
        stagger: 0.1,
        scrollTrigger: {
          trigger: creationsSection.value,
          start: 'top 80%',
          toggleActions: 'play none none none'
        }
      })

      // Floating circles animatie
      gsap.to('.circle-1', {
        x: 20,
        y: 30,
        duration: 5,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut'
      })

      gsap.to('.circle-2', {
        x: -15,
        y: -20,
        duration: 6,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut'
      })

      gsap.to('.circle-3', {
        x: 10,
        y: -15,
        duration: 4,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut'
      })
    })

    return {
      textContent,
      imageCircle,
      aboutSection,
      expertiseSection,
      creationsSection,
      expertises,
      projects,
      navigateTo,
      hoverExpertise,
      resetExpertise,
      hoverProject,
      resetProject
    }
  }
}
</script>

<style scoped>
.home-view {
  position: relative;
  overflow-x: hidden;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Hero Sectie */
.hero-section {
  padding: 80px 0;
  position: relative;
  background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ed 100%);
}

.hero-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
}

.text-content {
  flex: 1;
  max-width: 600px;
}

.welcome-text {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 20px;
  background: linear-gradient(90deg, #3a7bd5, #00d2ff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  line-height: 1.2;
}

.intro-text {
  font-size: 1.2rem;
  line-height: 1.6;
  color: #555;
  margin-bottom: 30px;
}

.story-button {
  background: linear-gradient(90deg, #3a7bd5, #00d2ff);
  color: white;
  border: none;
  padding: 12px 30px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  box-shadow: 0 4px 15px rgba(58, 123, 213, 0.3);
}

.story-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(58, 123, 213, 0.4);
}

.story-button:active {
  transform: translateY(1px);
}

.button-arrow {
  margin-left: 8px;
  transition: transform 0.3s ease;
}

.story-button:hover .button-arrow {
  transform: translateX(5px);
}

.image-circle {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  overflow: hidden;
  border: 5px solid white;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  position: relative;
  flex-shrink: 0;
}

.profile-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Sectie Styling */
.section-title {
  font-size: 2.5rem;
  text-align: center;
  margin-bottom: 50px;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, #3a7bd5, #00d2ff);
  border-radius: 2px;
}

.about-section {
  padding: 100px 0;
  background-color: white;
}

.about-text {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #555;
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.expertise-section {
  padding: 100px 0;
  background-color: #f9f9f9;
}

.expertise-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
}

.expertise-item {
  background: white;
  padding: 30px;
  border-radius: 15px;
  text-align: center;
  transition: all 0.3s ease;
  box-shadow: 0 5px 15px rgba(0,0,0,0.05);
}

.expertise-item:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0,0,0,0.1);
}

.expertise-icon {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  margin: 0 auto 20px;
  transition: all 0.3s ease;
}

.expertise-item h3 {
  font-size: 1.3rem;
  margin-bottom: 10px;
  transition: color 0.3s ease;
}

.creations-section {
  padding: 100px 0;
  background-color: white;
}

.creations-intro {
  text-align: center;
  font-size: 1.1rem;
  color: #666;
  margin-bottom: 40px;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
}

.project-card {
  background: white;
  border-radius: 15px;
  padding: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid #eee;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.project-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(58, 123, 213, 0.1) 0%, rgba(0, 210, 255, 0.1) 100%);
  z-index: -1;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.project-card:hover::before {
  opacity: 1;
}

.project-card h3 {
  font-size: 1.3rem;
  margin-bottom: 15px;
  color: #333;
}

.project-description {
  color: #666;
  margin-bottom: 20px;
  font-size: 0.95rem;
}

.project-link {
  color: #3a7bd5;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  transition: all 0.3s ease;
}

.project-card:hover .project-link {
  transform: translateX(5px);
}

.project-link::after {
  content: '→';
  margin-left: 5px;
  transition: transform 0.3s ease;
}

.project-card:hover .project-link::after {
  transform: translateX(5px);
}

/* Floating elements */
.floating-elements {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: -1;
  overflow: hidden;
}

.floating-circle {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.2;
}

.circle-1 {
  width: 300px;
  height: 300px;
  background: #3a7bd5;
  top: 10%;
  left: 5%;
}

.circle-2 {
  width: 400px;
  height: 400px;
  background: #00d2ff;
  bottom: 10%;
  right: 5%;
}

.circle-3 {
  width: 200px;
  height: 200px;
  background: #ff6b6b;
  top: 50%;
  left: 30%;
}

/* Responsive aanpassingen */
@media (max-width: 992px) {
  .hero-content {
    flex-direction: column;
    text-align: center;
  }

  .text-content {
    max-width: 100%;
    margin-bottom: 40px;
  }

  .welcome-text {
    font-size: 2.8rem;
  }
}

@media (max-width: 768px) {
  .welcome-text {
    font-size: 2.2rem;
  }

  .section-title {
    font-size: 2rem;
  }

  .expertise-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 576px) {
  .hero-section {
    padding: 60px 0;
  }

  .welcome-text {
    font-size: 1.8rem;
  }

  .intro-text {
    font-size: 1rem;
  }

  .expertise-grid {
    grid-template-columns: 1fr;
  }

  .image-circle {
    width: 250px;
    height: 250px;
  }
}
</style>
