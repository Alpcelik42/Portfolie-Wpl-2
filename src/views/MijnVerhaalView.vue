<template>
  <div class="story-view">
    <!-- Hero Sectie -->
    <section class="story-hero">
      <div class="container">
        <h1 class="hero-title" ref="heroTitle">Mijn Verhaal</h1>
        <p class="hero-subtitle" ref="heroSubtitle">Een reis door mijn opleiding en carrière tot nu toe.</p>
      </div>
    </section>

    <!-- Verhaal Timeline -->
    <div class="timeline-container">
      <!-- Timeline lijn -->
      <div class="timeline-line" ref="timelineLine"></div>

      <!-- Geboorte -->
      <div class="story-section left" ref="birthSection">
        <div class="story-content">
          <div class="text-content">
            <h2 class="story-title">Geboorte</h2>
            <p class="story-text">
              Ik ben geboren op 21 augustus 2004 in Utrecht, Nederland. Het was een dag vol nieuwe hoop en verwachtingen. Utrecht, met zijn mooie grachten en rijke geschiedenis, werd mijn eerste thuis. Toch groeide ik op in een gezin dat niet altijd alle financiële middelen had, maar waarin liefde en veerkracht centraal stonden. Hoewel armoede een deel van mijn jeugd was, overheersde het niet alles. Het betekende dat we soms creatief moesten zijn en keuzes moesten maken, maar mijn ouders zorgden ervoor dat ik nooit echt iets tekortkwam dat echt belangrijk was.
            </p>
          </div>
          <div class="image-container">
            <div class="story-circle">
              <img src="@/assets/images/20211024_151059.jpg" alt="Geboorte" class="story-image" />
            </div>
            <div class="timeline-dot"></div>
          </div>
        </div>
      </div>

      <!-- Eerste stappen -->
      <div class="story-section right" ref="firstStepsSection">
        <div class="story-content">
          <div class="text-content">
            <h2 class="story-title">Eerste stappen in mijn leven</h2>
            <p class="story-text">
              Ik werd geboren in Utrecht, Nederland, maar door financiële uitdagingen verhuisden we naar België om een beter leven op te bouwen. Deze stap bracht ons stabiliteit, maar betekende ook veranderingen. Tussen mijn tiende en twaalfde woonde ik bij mijn oma in Turkije. Daar leerde ik zelfstandig te zijn en voor mezelf te zorgen. Het was een periode vol uitdagingen, maar ook een tijd waarin ik veel over mezelf ontdekte. Toen ik terugkeerde naar België, voelde ik me sterker en volwassener. Deze ervaringen hebben me gevormd tot de persoon die ik nu ben: veerkrachtig en zelfstandig.
            </p>
          </div>
          <div class="image-container">
            <div class="story-circle">
              <img src="@/assets/images/20230329_151201.jpg" alt="Eerste stappen" class="story-image" />
            </div>
            <div class="timeline-dot"></div>
          </div>
        </div>
      </div>

      <!-- Eerste diploma -->
      <div class="story-section left" ref="firstDiplomaSection">
        <div class="story-content">
          <div class="text-content">
            <h2 class="story-title">Eerste diploma</h2>
            <p class="story-text">
              Na alle uitdagingen en ervaringen in mijn jonge jaren voelde het behalen van mijn eerste diploma als een enorme mijlpaal. Ondanks de moeilijkheden waarmee ik ben opgegroeid, wist ik door te zetten en mijn middelbare school succesvol af te ronden. Ik studeerde aan het Sint-Franciscuscollege.
            </p>
          </div>
          <div class="image-container">
            <div class="story-circle">
              <img src="@/assets/images/Sint-franciscus-college.jpg" alt="Eerste diploma" class="story-image" />
            </div>
            <div class="timeline-dot"></div>
          </div>
        </div>
      </div>

      <!-- Tweede diploma -->
      <div class="story-section right" ref="secondDiplomaSection">
        <div class="story-content">
          <div class="text-content">
            <h2 class="story-title">Tweede diploma</h2>
            <p class="story-text">
              Na mijn eerste diploma besloot ik mijn droom te volgen en begon ik mijn bachelor aspirant-lijnpiloot aan IPCA in Antwerpen. De opleiding was duur, en door financiële problemen moest ik samenwerken met een luchtvaartmaatschappij. Na veel gesprekken bood Corendon mij de kans, op voorwaarde dat ik een contract van 8 jaar zou tekenen en al mijn verdiensten aan hen zou afdragen om de opleiding terug te betalen. Het was een zware tijd. Ik werkte 3 tot 4 dagen per week voor Corendon, vervulde verschillende functies zoals stewardess en boarding agent, terwijl ik mijn studie volgde. Het was moeilijk, maar ik volhardde en behaalde mijn diploma als lijnpiloot. Hoewel mijn opleiding nog steeds niet volledig is afbetaald, werk ik nog steeds voor Corendon om de kosten terug te betalen. Het behalen van mijn diploma als lijnpiloot was de beloning voor alles wat ik heb doorstaan. Het heeft me niet alleen mijn droom dichterbij gebracht, maar ook laten zien dat je met vastberadenheid en hard werken elke uitdaging kunt overwinnen.
            </p>
          </div>
          <div class="image-container">
            <div class="story-circle">
              <img src="@/assets/images/139004092022.jpg" alt="Tweede diploma" class="story-image" />
            </div>
            <div class="timeline-dot"></div>
          </div>
        </div>
      </div>


      <!-- Back to School -->
      <div class="story-section left" ref="backToSchoolSection">
        <div class="story-content">
          <div class="text-content">
            <h2 class="story-title">Back to School</h2>
            <p class="story-text">
              Hoewel ik nog steeds een contract van 8 jaar heb bij Corendon, waarvan er nog maar 3 jaar over zijn, weet ik dat ik die tijd moet doorstaan. Nu dat ik mijn diploma heb behaald werk ik tussentijd als 2de kapitein piloot. Het is een uitdaging, maar het is nodig om mijn contract af te maken voordat ik een nieuw contract kan afsluiten bij een andere maatschappij als lijnpiloot. Om de tijd sneller te laten gaan en mezelf verder te ontwikkelen, ben ik begonnen aan een graduaatopleiding Digitale Vormgeving aan de Hogeschool PXL. Deze opleiding biedt me de kans om nieuwe vaardigheden te leren en de drie resterende jaren effectiever te benutten. Het is een nieuwe kleine opleinding dat wel mij goed laat voelen.
            </p>
          </div>
          <div class="image-container">
            <div class="story-circle">
              <img src="@/assets/images/pxl-logo.png" alt="Back to School" class="story-image" />
            </div>
            <div class="timeline-dot"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- CV Download Sectie -->
    <section class="cv-section" ref="cvSection">
      <div class="container">
        <div class="cv-content">
          <div class="cv-image-container">
            <div class="cv-circle">
              <img src="@/assets/images/cv.png" alt="CV Foto" class="cv-image" />
            </div>
          </div>
          <div class="cv-text-content">
            <h2 class="cv-title">Download mijn CV</h2>
            <p class="cv-text">Klik hieronder om mijn volledige CV te downloaden en meer te weten te komen over mijn ervaringen en vaardigheden.</p>
            <button @click="downloadCV" class="cv-button">
              Download CV
              <span class="download-icon">↓</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Opleiding en Werkervaring -->
    <section class="education-experience-section" ref="eduExpSection">
      <div class="container">
        <h2 class="section-title">Mijn Opleiding en Werkervaring</h2>
        <div class="columns-container">
          <div class="column education-column">
            <h3 class="column-title">Opleiding</h3>
            <div class="timeline-item" v-for="(edu, index) in education" :key="'edu-'+index">
              <div class="timeline-period">{{ edu.period }}</div>
              <div class="timeline-content">
                <h4 class="timeline-title">{{ edu.title }}</h4>
                <p class="timeline-description">{{ edu.description }}</p>
              </div>
            </div>
          </div>
          <div class="column experience-column">
            <h3 class="column-title">Werkervaring</h3>
            <div class="timeline-item" v-for="(exp, index) in experience" :key="'exp-'+index">
              <div class="timeline-period">{{ exp.period }}</div>
              <div class="timeline-content">
                <h4 class="timeline-title">{{ exp.title }}</h4>
                <p class="timeline-description">{{ exp.description }}</p>
              </div>
            </div>
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
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

export default {
  name: 'StoryView',
  setup() {
    const heroTitle = ref(null)
    const heroSubtitle = ref(null)
    const timelineLine = ref(null)
    const birthSection = ref(null)
    const firstStepsSection = ref(null)
    const firstDiplomaSection = ref(null)
    const secondDiplomaSection = ref(null)
    const darkChapterSection = ref(null)
    const freshStartSection = ref(null)
    const backToSchoolSection = ref(null)
    const cvSection = ref(null)
    const eduExpSection = ref(null)

    const education = ref([
      { period: '2014-2020', title: 'Secundaire Onderwijs', description: 'Sint-Franciscuscollege' },
      { period: '2020-2021', title: 'Avond onderwijs', description: 'Start to ICT' },
      { period: '2022-2023', title: 'Avond onderwijs', description: 'Advanced Programmeren' },
      { period: '2020-2023', title: 'Professionele bachelor', description: 'Aspirant-lijnpiloot' }
    ])

    const experience = ref([
      { period: '2020-2021', title: 'Corendon', description: 'Loader en boarding agent' },
      { period: '2021-2022', title: 'Corendon', description: 'Stewardess' }
    ])

    const downloadCV = () => {
      // Hier zou je normaal een PDF downloaden
      // Voor nu simuleren we het met een alert
      alert('CV download zou nu starten')
    }

    onMounted(() => {
      // Hero animatie
      gsap.from(heroTitle.value, {
        opacity: 0,
        y: -30,
        duration: 0.8,
        ease: 'power2.out'
      })

      gsap.from(heroSubtitle.value, {
        opacity: 0,
        y: 30,
        duration: 0.8,
        delay: 0.3,
        ease: 'power2.out'
      })

      // Timeline lijn animatie
      gsap.from(timelineLine.value, {
        scaleY: 0,
        duration: 2,
        scrollTrigger: {
          trigger: timelineLine.value,
          start: 'top 80%',
          toggleActions: 'play none none none'
        },
        ease: 'power2.out'
      })

      // Sectie animaties
      const sections = [
        birthSection.value,
        firstStepsSection.value,
        firstDiplomaSection.value,
        secondDiplomaSection.value,
        darkChapterSection.value,
        freshStartSection.value,
        backToSchoolSection.value
      ]

      sections.forEach((section, index) => {
        gsap.from(section, {
          opacity: 0,
          x: index % 2 === 0 ? -100 : 100,
          duration: 0.8,
          scrollTrigger: {
            trigger: section,
            start: 'top 75%',
            toggleActions: 'play none none none'
          },
          ease: 'power2.out'
        })
      })

      // CV sectie animatie
      gsap.from(cvSection.value, {
        opacity: 0,
        y: 50,
        duration: 0.8,
        scrollTrigger: {
          trigger: cvSection.value,
          start: 'top 75%',
          toggleActions: 'play none none none'
        },
        ease: 'power2.out'
      })

      // Opleiding/werkervaring animatie
      gsap.from(eduExpSection.value, {
        opacity: 0,
        y: 50,
        duration: 0.8,
        scrollTrigger: {
          trigger: eduExpSection.value,
          start: 'top 75%',
          toggleActions: 'play none none none'
        },
        ease: 'power2.out'
      })

      gsap.from('.timeline-item', {
        opacity: 0,
        y: 20,
        duration: 0.5,
        stagger: 0.1,
        scrollTrigger: {
          trigger: eduExpSection.value,
          start: 'top 75%',
          toggleActions: 'play none none none'
        },
        ease: 'power2.out'
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
      heroTitle,
      heroSubtitle,
      timelineLine,
      birthSection,
      firstStepsSection,
      firstDiplomaSection,
      secondDiplomaSection,
      darkChapterSection,
      freshStartSection,
      backToSchoolSection,
      cvSection,
      eduExpSection,
      education,
      experience,
      downloadCV
    }
  }
}
</script>

<style scoped>
.story-view {
  position: relative;
  overflow-x: hidden;
  background-color: #f9f9f9;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Hero Sectie */
.story-hero {
  padding: 120px 0 80px;
  text-align: center;
  background: linear-gradient(135deg, #3a7bd5, #00d2ff);
  color: white;
  position: relative;
  overflow: hidden;
}

.hero-title {
  font-size: 4rem;
  font-weight: 700;
  margin-bottom: 20px;
  position: relative;
  z-index: 2;
}

.hero-subtitle {
  font-size: 1.5rem;
  max-width: 700px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

/* Timeline Container */
.timeline-container {
  position: relative;
  padding: 80px 0;
}

.timeline-line {
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 4px;
  background: linear-gradient(to bottom, #3a7bd5, #00d2ff);
  transform: translateX(-50%);
  z-index: 1;
}

/* Story Secties */
.story-section {
  position: relative;
  margin-bottom: 80px;
  z-index: 2;
}

.story-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  max-width: 1100px;
  margin: 0 auto;
  position: relative;
}

.left .story-content {
  flex-direction: row;
}

.right .story-content {
  flex-direction: row-reverse;
}

.text-content {
  flex: 1;
  padding: 30px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  position: relative;
  z-index: 2;
}

.image-container {
  position: relative;
  flex-shrink: 0;
  width: 300px;
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.story-circle {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
  border: 5px solid white;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  position: relative;
}

.story-circle.dark {
  filter: brightness(0.8);
}

.story-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.timeline-dot {
  position: absolute;
  width: 20px;
  height: 20px;
  background: linear-gradient(135deg, #3a7bd5, #00d2ff);
  border-radius: 50%;
  border: 4px solid white;
  z-index: 3;
}

.left .timeline-dot {
  right: -10px;
}

.right .timeline-dot {
  left: -10px;
}

.story-title {
  font-size: 2rem;
  color: #333;
  margin-bottom: 20px;
  position: relative;
}

.story-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 0;
  width: 60px;
  height: 4px;
  background: linear-gradient(90deg, #3a7bd5, #00d2ff);
  border-radius: 2px;
}

.story-text {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #555;
}

/* CV Sectie */
.cv-section {
  padding: 80px 0;
  background: white;
}

.cv-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 60px;
  max-width: 900px;
  margin: 0 auto;
}

.cv-image-container {
  flex-shrink: 0;
}

.cv-circle {
  width: 250px;
  height: 250px;
  border-radius: 50%;
  overflow: hidden;
  border: 5px solid white;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.cv-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.cv-text-content {
  flex: 1;
}

.cv-title {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 20px;
}

.cv-text {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #555;
  margin-bottom: 30px;
}

.cv-button {
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

.cv-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(58, 123, 213, 0.4);
}

.cv-button:active {
  transform: translateY(1px);
}

.download-icon {
  margin-left: 8px;
  transition: transform 0.3s ease;
}

.cv-button:hover .download-icon {
  transform: translateY(3px);
}

/* Opleiding en Werkervaring */
.education-experience-section {
  padding: 80px 0;
  background: #f9f9f9;
}

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

.columns-container {
  display: flex;
  gap: 40px;
  max-width: 1000px;
  margin: 0 auto;
}

.column {
  flex: 1;
  background: white;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.05);
}

.column-title {
  font-size: 1.8rem;
  color: #333;
  margin-bottom: 30px;
  text-align: center;
  position: relative;
}

.column-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #3a7bd5, #00d2ff);
  border-radius: 2px;
}

.education-column .column-title::after {
  background: linear-gradient(90deg, #3a7bd5, #00d2ff);
}

.experience-column .column-title::after {
  background: linear-gradient(90deg, #00d2ff, #3a7bd5);
}

.timeline-item {
  position: relative;
  padding-left: 30px;
  margin-bottom: 30px;
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: 0;
  top: 5px;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background: linear-gradient(135deg, #3a7bd5, #00d2ff);
}

.education-column .timeline-item::before {
  background: linear-gradient(135deg, #3a7bd5, #00d2ff);
}

.experience-column .timeline-item::before {
  background: linear-gradient(135deg, #00d2ff, #3a7bd5);
}

.timeline-period {
  font-weight: 600;
  color: #3a7bd5;
  margin-bottom: 5px;
}

.education-column .timeline-period {
  color: #3a7bd5;
}

.experience-column .timeline-period {
  color: #00d2ff;
}

.timeline-title {
  font-size: 1.2rem;
  color: #333;
  margin-bottom: 5px;
}

.timeline-description {
  color: #666;
  font-size: 0.95rem;
  line-height: 1.6;
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
  opacity: 0.15;
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

/* Responsieve aanpassingen */
@media (max-width: 992px) {
  .story-content {
    flex-direction: column !important;
    max-width: 600px;
  }

  .image-container {
    margin: 30px 0;
  }

  .left .timeline-dot, .right .timeline-dot {
    left: 50%;
    top: -10px;
    transform: translateX(-50%);
  }

  .columns-container {
    flex-direction: column;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 3rem;
  }

  .hero-subtitle {
    font-size: 1.2rem;
  }

  .story-title {
    font-size: 1.8rem;
  }

  .cv-content {
    flex-direction: column;
    text-align: center;
  }

  .cv-title {
    font-size: 2rem;
  }
}

@media (max-width: 576px) {
  .hero-title {
    font-size: 2.2rem;
  }

  .story-text, .cv-text {
    font-size: 1rem;
  }

  .image-container {
    width: 250px;
    height: 250px;
  }

  .cv-circle {
    width: 200px;
    height: 200px;
  }

  .section-title {
    font-size: 2rem;
  }

  .column-title {
    font-size: 1.5rem;
  }
}
</style>
