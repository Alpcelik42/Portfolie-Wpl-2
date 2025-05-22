<template>
  <div class="expertise-view">
    <!-- Hero Sectie -->
    <section class="expertise-hero">
      <div class="container">
        <h1 class="hero-title">Expertise</h1>
        <p class="hero-subtitle">Ontdek mijn vaardigheden en ervaring in front-end en back-end development.</p>
      </div>
    </section>

    <!-- Vaardigheden & Ervaring Sectie -->
    <section class="skills-section">
      <div class="container">
        <h2 class="section-title">Vaardigheden & Ervaring</h2>
        <p class="section-text">
          Mijn expertise omvat zowel front-end als back-end development, met een focus op het ontwikkelen van intuïtieve en dynamische webervaringen.
          Als student in digitale vormgeving ben ik bedreven in een breed scala aan technologieën, waaronder HTML5, CSS3, JavaScript, Python, Rust, Dart,
          Cisco Packet Tracer en MySQL. Daarnaast gebruik ik tools zoals Visual Studio Code, Figma, Git, Photoshop en Illustrator om visueel aantrekkelijke
          en technisch sterke projecten te realiseren. Ik ontwerp gebruiksvriendelijke interfaces, ontwikkel robuuste applicaties, en automatiseer processen
          om efficiënte oplossingen te creëren. Mijn passie ligt in het combineren van creativiteit en techniek om innovatieve producten te bouwen.
          Voor meer informatie, neem contact op.
        </p>
      </div>
    </section>

    <!-- Tools Carousel Sectie -->
    <section class="tools-section">
      <div class="container">
        <h2 class="section-title">Tools</h2>
        <div class="tools-carousel">
          <div class="tools-track" ref="toolsTrack">
            <div class="tool-item" v-for="(tool, index) in tools" :key="index">
              <img :src="tool.image" :alt="tool.name" class="tool-image" />
              <p class="tool-name">{{ tool.name }}</p>
            </div>
            <!-- Dupliceren voor oneindige loop -->
            <div class="tool-item" v-for="(tool, index) in tools" :key="index + tools.length">
              <img :src="tool.image" :alt="tool.name" class="tool-image" />
              <p class="tool-name">{{ tool.name }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Favoriete Tools Sectie -->
    <section class="favorite-tools-section">
      <div class="container">
        <h2 class="section-title">Favoriete 3 Tools</h2>

        <div class="favorite-tools">
          <!-- HTML5 -->
          <div class="favorite-tool">
            <div class="tool-number">1</div>
            <div class="tool-content">
              <h3 class="tool-title">HTML5</h3>
              <p class="tool-description">
                HTML (HyperText Markup Language) vormt de basis van elke webpagina. Ik ben zeer ervaren in het structureren van inhoud en het creëren van semantische, toegankelijke webpagina's. Van eenvoudige sites tot complexe layouts, ik gebruik HTML om robuuste en toekomstbestendige structuren te bouwen.
              </p>
            </div>
          </div>

          <!-- JavaScript -->
          <div class="favorite-tool">
            <div class="tool-number">2</div>
            <div class="tool-content">
              <h3 class="tool-title">JavaScript</h3>
              <p class="tool-description">
                Met JavaScript breng ik dynamiek en interactiviteit naar websites. Van geavanceerde animaties tot complexe logica en API-integraties, mijn kennis stelt me in staat om gebruiksvriendelijke en functionele webtoepassingen te ontwikkelen. JavaScript is mijn krachtigste tool om ideeën tot leven te brengen.
              </p>
            </div>
          </div>

          <!-- Python -->
          <div class="favorite-tool">
            <div class="tool-number">3</div>
            <div class="tool-content">
              <h3 class="tool-title">Python</h3>
              <p class="tool-description">
                Python gebruik ik voor data-analyse, automatisering en back-end ontwikkeling. Dankzij de veelzijdigheid van de taal kan ik efficiënt scripts en toepassingen schrijven die complexe problemen oplossen. Ik gebruik frameworks zoals Flask en Django om krachtige webservices te creëren.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import gsap from 'gsap'

export default {
  name: 'ExpertiseView',
  setup() {
    const toolsTrack = ref(null)

    const tools = ref([
      { name: 'HTML5', image: 'assets/images/html5.png' },
      { name: 'CSS3', image: 'assets/images/css3.png' },
      { name: 'JavaScript', image: 'assets/images/javascript.png' },
      { name: 'Python', image: 'assets/images/Python.png' },
      { name: 'Rust', image: 'assets/images/rust.png' },
      { name: 'Dart', image: 'assets/images/dart.png' },
      { name: 'MySQL', image: 'assets/images/mysql.png' },
      { name: 'VS Code', image: 'assets/images/visualstudiocode.png' },
      { name: 'Figma', image: 'assets/images/figma.png' },
      { name: 'Git', image: 'assets/images/git.png' },
      { name: 'Photoshop', image: 'assets/images/photoshop.png' },
      { name: 'Illustrator', image: 'assets/images/Illustrator.png' },
      { name: 'Cisco', image: 'assets/images/Cisco.png' }
    ])

    onMounted(() => {
      const trackWidth = toolsTrack.value.scrollWidth / 2
      gsap.to(toolsTrack.value, {
        x: -trackWidth,
        duration: 30,
        repeat: -1,
        ease: 'none'
      })


      gsap.utils.toArray('.section-title, .section-text, .favorite-tool').forEach(element => {
        gsap.from(element, {
          opacity: 0,
          y: 50,
          duration: 0.8,
          scrollTrigger: {
            trigger: element,
            start: 'top 80%',
            toggleActions: 'play none none none'
          },
          ease: 'power2.out'
        })
      })
    })

    return {
      tools,
      toolsTrack
    }
  }
}
</script>

<style scoped>
.expertise-view {
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
.expertise-hero {
  padding: 120px 0 80px;
  text-align: left;
  background: linear-gradient(130deg, #3a7bd5, #2ecc71 );
  color: white;
  position: relative;
  overflow: hidden;
}

.hero-title {
  font-size: 4rem;
  font-weight: 700;
  margin-bottom: 20px;
  position: relative;
}

.hero-subtitle {
  font-size: 1.5rem;
  max-width: 700px;
  position: relative;
}

/* Vaardigheden Sectie */
.skills-section {
  padding: 80px 0;
  background: white;
}

.section-title {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 30px;
  position: relative;
  display: inline-block;
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

.section-text {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #555;
  max-width: 900px;
}

/* Tools Sectie */
.tools-section {
  padding: 80px 0;
  background: #f9f9f9;
  overflow: hidden;
}

.tools-carousel {
  width: 100%;
  overflow: hidden;
  position: relative;
}

.tools-track {
  display: flex;
  gap: 40px;
  padding: 20px 0;
  width: max-content;
}

.tool-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 120px;
}

.tool-image {
  width: 80px;
  height: 80px;
  object-fit: contain;
  margin-bottom: 15px;
  transition: transform 0.3s ease;
}

.tool-item:hover .tool-image {
  transform: scale(1.1);
}

.tool-name {
  font-weight: 600;
  color: #333;
  text-align: center;
}

/* Favoriete Tools Sectie */
.favorite-tools-section {
  padding: 80px 0;
  background: white;
}

.favorite-tools {
  display: flex;
  flex-direction: column;
  gap: 40px;
  max-width: 900px;
  margin: 0 auto;
}

.favorite-tool {
  display: flex;
  gap: 30px;
  background: #f9f9f9;
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.05);
  transition: transform 0.3s ease;
}

.favorite-tool:hover {
  transform: translateY(-5px);
}

.tool-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #3a7bd5;
  min-width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  border-radius: 50%;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.tool-content {
  flex: 1;
}

.tool-title {
  font-size: 1.8rem;
  color: #333;
  margin-bottom: 15px;
}

.tool-description {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #555;
}

/* Responsieve aanpassingen */
@media (max-width: 992px) {
  .hero-title {
    font-size: 3rem;
  }

  .hero-subtitle {
    font-size: 1.2rem;
  }

  .section-title {
    font-size: 2rem;
  }

  .tool-item {
    min-width: 100px;
  }

  .tool-image {
    width: 60px;
    height: 60px;
  }
}

@media (max-width: 768px) {
  .expertise-hero {
    padding: 80px 0 60px;
  }

  .hero-title {
    font-size: 2.5rem;
  }

  .favorite-tool {
    flex-direction: column;
    gap: 20px;
  }

  .tool-number {
    width: 50px;
    height: 50px;
    font-size: 2rem;
  }
}

@media (max-width: 576px) {
  .hero-title {
    font-size: 2rem;
  }

  .section-text, .tool-description {
    font-size: 1rem;
  }

  .tools-track {
    gap: 20px;
  }

  .tool-item {
    min-width: 80px;
  }

  .tool-image {
    width: 50px;
    height: 50px;
  }

  .tool-name {
    font-size: 0.9rem;
  }
}
</style>
