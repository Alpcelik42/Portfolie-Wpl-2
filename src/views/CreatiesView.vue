<template>
  <div class="creaties-view">
    <div v-if="!selectedCategory" class="category-selection">
      <h1 class="title">Mijn Creaties</h1>
      <div class="categories-container">
        <div
          class="category-card"
          @click="selectCategory('wpl1')"
          @mouseenter="hoverCategory('wpl1')"
          @mouseleave="resetHover"
        >

          <h2>WPL1 Projecten</h2>
          <p>Schoolprojecten uit het eerste trimester</p>
          <div class="hover-effect" :class="{ active: hoverState === 'wpl1' }"></div>
        </div>

        <div
          class="category-card"
          @click="selectCategory('personal')"
          @mouseenter="hoverCategory('personal')"
          @mouseleave="resetHover"
        >
          <h2>Persoonlijke Projecten</h2>
          <p>Projecten die ik in mijn vrije tijd heb gemaakt</p>
          <div class="hover-effect" :class="{ active: hoverState === 'personal' }"></div>
        </div>

        <div
          class="category-card"
          @click="selectCategory('wpl2')"
          @mouseenter="hoverCategory('wpl2')"
          @mouseleave="resetHover"
        >
          <h2>WPL2 Project</h2>
          <p>Portfolio website ontwikkeling</p>
          <div class="hover-effect" :class="{ active: hoverState === 'wpl2' }"></div>
        </div>
      </div>
    </div>

    <div v-else class="projects-container">
      <button class="back-button" @click="goBack">
        <span>&larr;</span> Terug naar overzicht
      </button>

      <div v-if="selectedCategory === 'wpl1'" class="wpl1-projects">
        <h1 class="section-title">WPL1 Projecten</h1>

        <div class="view-toggle">
          <button @click="toggleView('grid')" :class="{ active: currentView === 'grid' }">Grid Weergave</button>
          <button @click="toggleView('list')" :class="{ active: currentView === 'list' }">Lijst Weergave</button>
        </div>

        <div v-if="currentView === 'grid'" class="projects-grid">
          <div
            v-for="(project, index) in wpl1Projects"
            :key="project.id"
            class="project-card"
            :style="{ 'animation-delay': `${index * 0.1}s` }"
          >
            <div class="project-image">
              <img :src="getImageUrl(project.image)" :alt="project.title">
            </div>
            <div class="project-content">
              <h3>{{ project.title }}</h3>
              <p>{{ project.description }}</p>
              <p><strong>Technologieën:</strong> {{ project.technologies }}</p>
              <div class="project-links">
                <a
                  v-for="(link, i) in project.links"
                  :key="i"
                  :href="link.url"
                  :class="link.class"
                  :download="link.download ? getFileName(link.url) : null"
                  target="_blank"
                >
                  {{ link.text }}
                </a>
              </div>
            </div>
          </div>
        </div>

        <div v-if="currentView === 'list'" class="projects-list">
          <div
            v-for="(project, index) in wpl1Projects"
            :key="project.id"
            class="project-list-item"
            :style="{ 'animation-delay': `${index * 0.1}s` }"
          >
            <div class="list-item-content">
              <div class="list-item-image">
                <img :src="getImageUrl(project.image)" :alt="project.title">
              </div>
              <div class="list-item-details">
                <h3>{{ project.title }}</h3>
                <p><strong>Technologieën:</strong> {{ project.technologies }}</p>
                <p>{{ project.description }}</p>
                <div class="project-links">
                  <a
                    v-for="(link, i) in project.links"
                    :key="i"
                    :href="link.url"
                    :class="link.class"
                    :download="link.download ? getFileName(link.url) : null"
                    target="_blank"
                  >
                    {{ link.text }}
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-if="selectedCategory === 'personal'" class="personal-projects">
        <h1 class="section-title">Persoonlijke Projecten</h1>

        <div class="view-toggle">
          <button @click="toggleView('grid')" :class="{ active: currentView === 'grid' }">Grid Weergave</button>
          <button @click="toggleView('list')" :class="{ active: currentView === 'list' }">Lijst Weergave</button>
        </div>

        <div v-if="currentView === 'grid'" class="projects-grid">
          <div
            v-for="(project, index) in personalProjects"
            :key="project.id"
            class="project-card"
            :style="{ 'animation-delay': `${index * 0.1}s` }"
          >
            <div class="project-image">
              <img :src="getImageUrl(project.image)" :alt="project.title">
            </div>
            <div class="project-content">
              <h3>{{ project.title }}</h3>
              <p>{{ project.description }}</p>
              <p><strong>Technologieën:</strong> {{ project.technologies }}</p>
              <div class="project-links">
                <a
                  v-for="(link, i) in project.links"
                  :key="i"
                  :href="link.url"
                  :class="link.class"
                  :download="link.download ? getFileName(link.url) : null"
                  target="_blank"
                >
                  {{ link.text }}
                </a>
              </div>
            </div>
          </div>
        </div>

        <div v-if="currentView === 'list'" class="projects-list">
          <div
            v-for="(project, index) in personalProjects"
            :key="project.id"
            class="project-list-item"
            :style="{ 'animation-delay': `${index * 0.1}s` }"
          >
            <div class="list-item-content">
              <div class="list-item-image">
                <img :src="getImageUrl(project.image)" :alt="project.title">
              </div>
              <div class="list-item-details">
                <h3>{{ project.title }}</h3>
                <p><strong>Technologieën:</strong> {{ project.technologies }}</p>
                <p>{{ project.description }}</p>
                <div class="project-links">
                  <a
                    v-for="(link, i) in project.links"
                    :key="i"
                    :href="link.url"
                    :class="link.class"
                    :download="link.download ? getFileName(link.url) : null"
                    target="_blank"
                  >
                    {{ link.text }}
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-if="selectedCategory === 'wpl2'" class="wpl2-projects">
        <h1 class="section-title">WPL2 Project</h1>
        <div class="wpl2-case">
          <div class="case-header">
            <h2>Portfolio Website Development</h2>
            <div class="case-image">
              <img src="@/assets/images/E-taalent.png" alt="Portfolio Screenshot">
            </div>
          </div>

          <div class="case-section">
            <h3>Case Beschrijving</h3>
            <p>
              E-taalent is een organisatie die zowel taaltrainingen (Nederlands en Frans, zakelijk taalgebruik) aanbiedt als workshops rond digitale onderwijstools. De trainingen zijn gericht op bedrijven, particulieren én onderwijsprofessionals. De ‘E’ in E-taalent verwijst naar de digitale focus: blended learning, AI in het onderwijs, inclusief onderwijs en het gebruik van tools als Google Workspace, Kahoot, H5P en Moodle. Onze opdracht bestond uit het ontwerpen en ontwikkelen van een digitale totaaloplossing voor E-taalent, met een professionele huisstijl, een aantrekkelijke website als visitekaartje, en functionele integraties zoals een leeromgeving, boekingsmodaliteiten en webinar-ondersteuning.
              <br><br>
              De klant vroeg specifiek om een herziening van de huisstijl (logo, visuals, video thumbnails, ...), een gestructureerde en gebruiksvriendelijke website, een beveiligde sectie voor leermateriaal, en integratie van een online winkel en videoconferencingtools zoals Zoom. Onze taak was om dit alles uit te werken in een dynamisch en functioneel platform.            </p>
          </div>

          <div class="case-section">
            <h3>Mijn Aandeel</h3>
            <p>
              Mijn verantwoordelijkheid lag op meerdere vlakken:
              <br><br>
              Ik zorgde ervoor dat de GitHub-omgeving volledig werd opgezet, inclusief het uitnodigen van teamleden, het structureren van de repositories en het bijhouden van de voortgang.
              Ik nam de leiding in het opzetten van de coding-omgevingen, zodat alle teamleden efficiënt konden samenwerken.
              Ik werkte actief mee aan de frontend in HTML/CSS/Vue.js, waar ik verantwoordelijk was voor componenten zoals de Header en Footer, en het implementeren van het wireframe-design.
              Verder hielp ik bij het integreren van de backend, zodat onder andere login en wachtwoordreset functioneel werkten (ook getest via Postman).
              In latere fases werkte ik mee aan het volledig dynamisch maken van de website, het oplossen van fouten en het testen van alle functionaliteiten.
              Tot slot leverde ik mijn deel van de documentatie, pitchpresentatie en portfolio tijdig in, waarin ik zowel mijn design- als developmentbijdrage toelicht.            </p>
          </div>

          <div class="case-section">
            <h3>Wat Ik Heb Geleerd</h3>
            <p>
              Deze case was zeer waardevol. Ik leerde niet alleen hoe ik in teamverband aan een echte opdracht werk, maar ook hoe belangrijk duidelijke communicatie en taakverdeling zijn. Technisch gezien verbeterde ik mijn vaardigheden in Vue.js en het structureren van component-based frontends. Ook leerde ik hoe ik een back-end koppel aan een frontend en hoe ik API’s test met tools als Postman.
              <br><br>
              Daarnaast kreeg ik inzicht in het belang van versiebeheer met GitHub in teamprojecten. Tot slot leerde ik hoe je een project professioneel presenteert via pitchslides en een individueel portfolio.            </p>
          </div>

          <div class="case-section deliverables">
            <h3>Deliverables</h3>
            <ul>
              <li>GitHub volledig in orde + teamleden uitgenodigd</li>
              <li>Coding-omgevingen volledig opgezet</li>
              <li>Teampagina aangemaakt én afgewerkt</li>
              <li>Inloggen en password reset werken in de front-end</li>
              <li>Eerste opzet van andere pagina's</li>
              <li>Controle van API door PRO</li>
              <li>HTML/CSS: wireframes/designs geïmplementeerd</li>
              <li>Components aangemaakt (Header, Footer, ...)</li>
              <li>Alle pagina's bestaan op GitHub én staan online</li>
              <li>CSS-bestanden, assets, links etc. correct toegevoegd</li>
              <li>Website is bruikbaar (functioneel, kleine schoonheidsfouten mogelijk)</li>
              <li>Back-end is geïntegreerd en werkt (bv. getest met Postman)</li>
              <li>Dynamische website volledig afgewerkt</li>
              <li>Website is online en up-to-date op GitHub</li>
              <li>Geen errors – alles werkt zoals verwacht</li>
            </ul>
            <div class="deliverable-links">
              <a href="https://github.com/PXL-WPL2-2425/wpl2-frontend-team_10.git" class="deliverable-link">Bekijk Live Website</a>
              <a href="#" class="deliverable-link">Download Documentatie</a>
              <a href="../assets/projecten/E-taalent%20pitch%20&%20demo.pptx" class="deliverable-link" download="E-taalent_pitch_&_demo.pptx">Bekijk Presentatie</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CreatiesView',
  data() {
    return {
      selectedCategory: null,
      hoverState: null,
      currentView: 'grid',
      wpl1Projects: [
        {
          id: 1,
          title: 'Werkveldverkenning - Seminaries',
          description: 'Tijdens deze seminaries kwamen vertegenwoordigers van bedrijven zoals Made, Monocode en Code Capital langs om hun werking toe te lichten. Ze vertelden over hun projecten, bedrijfsvisie en wat we kunnen verwachten als we daar zouden starten. Deze sessies boden een inspirerend kijkje in het werkveld en gaven me een beter beeld van de kansen en uitdagingen in de digitale vormgeving.',
          technologies: 'Word',
          image: 'seminaries.jpg',
          links: [
            {
              url: 'Alperen_Ozcelik_ReflectieSeminariesGastsprekers.pdf',
              text: 'Download PDF',
              class: 'download-link',
              download: true
            }
          ]
        },
        {
          id: 2,
          title: 'Werkveldverkenning - Vacatures',
          description: 'In deze opdracht heb ik verschillende vacatures binnen de digitale vormgeving geanalyseerd. Ik onderzocht onder andere het profiel van de functie, sterke en zwakke kanten van de job en de gevraagde vaardigheden. Deze analyse gaf me waardevolle inzichten in wat werkgevers zoeken en hielp me mijn eigen professionele doelen beter te definiëren.',
          technologies: 'Word, indeed en VDAB',
          image: 'vacature.jpg',
          links: [
            {
              url: 'Vacature1.pdf',
              text: 'Download PDF 1',
              class: 'download-link',
              download: true
            },
            {
              url: 'Vacature2.pdf',
              text: 'Download PDF 2',
              class: 'download-link',
              download: true
            },
            {
              url: 'Vacature3.pdf',
              text: 'Download PDF 3',
              class: 'download-link',
              download: true
            },
            {
              url: 'Vacature4.pdf',
              text: 'Download PDF 4',
              class: 'download-link',
              download: true
            },
            {
              url: 'Vacature5.pdf',
              text: 'Download PDF 5',
              class: 'download-link',
              download: true //
            }
          ]
        },
        {
          id: 3,
          title: 'Dashboard CV & Concept-Poster',
          description: 'Als onderdeel van een creatieve opdracht heb ik en mijn groep een interactief CV-dashboard ontworpen en een conceptposter gemaakt. Het CV biedt een overzicht van mijn vaardigheden, terwijl de poster mijn creatieve proces visualiseert.',
          technologies: 'Figma, Miro',
          image: 'Dashboard.png',
          links: [
            {
              url: 'https://www.figma.com/design/9nwtWRMAOLtxAjRCNWNE7V/cv-dashboard',
              text: 'Open Dashboard CV',
              class: 'demo-link'
            },
            {
              url: 'https://miro.com/app/board/uXjVLQflZ0w=/',
              text: 'Open Concept poster',
              class: 'demo-link'
            }
          ]
        },
        {
          id: 4,
          title: 'Visual Design Portfolio',
          description: 'In dit portfolio presenteer ik mijn meest creatieve en visueel aantrekkelijke projecten uit mijn opleiding Digitale Vormgeving. Het bevat ontwerpen waarin ik mijn vaardigheden in typografie, lay-out en grafisch design heb toegepast. Elk project laat zien hoe ik visuele communicatie combineer met esthetiek om een impactvolle ervaring te creëren. Dit portfolio is een weerspiegeling van mijn groei en passie voor design.',
          technologies: 'Figma',
          image: 'Dashboard.png',
          links: [
            {
              url: 'https://www.figma.com/design/pmmp7guG8ZLIg2yAYLK4f8/Untitled',
              text: 'Open Design Portfolio',
              class: 'demo-link'
            }
          ]
        },
        {
          id: 5,
          title: 'POP-sessies',
          description: 'De opdrachten gaven me waardevolle inzichten in mijn persoonlijke ontwikkeling. De eerste opdracht over personal branding hielp me mijn sterke punten en zwaktes te identificeren, en mijn balans tussen creativiteit en professionaliteit te begrijpen. De tweede opdracht over zelfreflectie en motivatie gaf me dieper inzicht in mijn drijfveren en kernwaarden, wat me hielp mijn doelen beter te begrijpen. De laatste opdracht met de STARR-methode stelde me in staat om mijn aanpak in groepsprojecten te analyseren en verbeterpunten te ontdekken.',
          technologies: 'Reflectie documenten',
          image: 'pop-sessions.jpg',
          links: [
            {
              url: 'AlperenOzcelikSituatie_1.pdf',
              text: 'Download Situatie 1',
              class: 'download-link',
              download: true
            },
            {
              url: 'AlperenOzcelikSituatie_2.pdf',
              text: 'Download Situatie 2',
              class: 'download-link',
              download: true
            }
          ]
        }
      ],
      personalProjects: [
        {
          id: 1,
          title: 'PlantBuddy',
          description: 'Als plantenliefhebber heb ik meegeholpen aan de ontwikkeling van de Plantsome app, een app die gebruikers helpt bij het bijhouden van hun plantverzorging. In dit project was ik verantwoordelijk voor het ontwerpen en ontwikkelen van verschillende functionaliteiten van de app, zoals het toevoegen van planten, het instellen van verzorgingsherinneringen en het aanbieden van tips voor plantverzorging. Door mijn interesse in planten kon ik me goed inleven in de behoeften van de gebruikers, wat hielp bij het creëren van een gebruiksvriendelijke interface.',
          technologies: 'JavaScript, Dart, Rust en Figma',
          image: 'Plantsome.png',
          links: [
            {
              url: 'https://play.google.com/store/apps/details?id=nl.plantsome.app&hl=nl',
              text: 'Download de app',
              class: 'demo-link'
            }
          ]
        },
        {
          id: 2,
          title: 'GroenteWinkel',
          description: 'Een interactieve groente- en fruitwinkel. Gebruikers kunnen de voedingswaarden van producten bekijken en bestellingen plaatsen.',
          technologies: 'HTML, CSS, JavaScript',
          image: 'groentewinkel.png',
          links: [
            {
              url: 'Groentewinkel.zip',
              text: 'Download volledig',
              class: 'download-link',
              download: true
            }
          ]
        },
        {
          id: 3,
          title: 'FlightManager',
          description: 'De opdracht was voor het vak Python en MySQL, waarin we een tool moesten ontwikkelen voor luchtvaartliefhebbers om vluchtinformatie en reisroutes te beheren. Ik was verantwoordelijk voor het opzetten van de database in MySQL, waarin vluchtgegevens zoals vertrek- en aankomsttijden, luchthavens, vliegtuigmaatschappijen en route-informatie werden opgeslagen. Vervolgens ontwikkelde ik een Python-script dat deze gegevens opvraagt en weergeeft via een gebruiksvriendelijke interface.',
          technologies: 'Python en MySQL',
          image: 'vluchtboekingen.png',
          links: [
            {
              url: 'Vluchten.zip',
              text: 'Download volledig',
              class: 'download-link',
              download: true
            }
          ]
        },
        {
          id: 4,
          title: 'Netwerkbeveiliging en Configuratie',
          description: 'In dit project gebruikte ik Cisco Packet Tracer om netwerkconfiguraties en beveiliging te implementeren. Ik verbond een computer met een webserver via HTTP en HTTPS, blokkeerde onversleutelde verbindingen, stelde een client-to-site VPN in voor veilige bestandsoverdracht, en configureerde een draadloos netwerk met beveiligde routers. Het project verbeterde mijn vaardigheden in netwerkbeheer en beveiliging.',
          technologies: 'Cisco packet tracer',
          image: 'ciscopacketracer.jpg',
          links: [
            {
              url: 'Packet_Tracer_6.4.1-Server_Firewalls_and_Router_and_Switch_Resilience.pka',
              text: 'Download project',
              class: 'download-link',
              download: true
            }
          ]
        },
        {
          id: 5,
          title: 'Kassasysteem voor Mosselfestijn',
          description: 'Dit schoolproject betrof het ontwikkelen van een kassasysteem voor een mosselfestijn in Python. De eerste opdracht berekende het totaalbedrag en bood de mogelijkheid om het kassaprogramma na elke bestelling te stoppen. De tweede opdracht voegde kortingen en een kassaticket toe met de bestel- en betaalinformatie. Het project gebruikte variabelen, conditionals, loops en functies. Iedereen in de klas had een soortgelijk project, maar met eigen focus en aanpassingen.',
          technologies: 'Python',
          image: 'Kassasysteem.png',
          links: [
            {
              url: 'MosseIfeestKorting.py',
              text: 'Download Deel 1',
              class: 'download-link',
              download: true
            },
            {
              url: 'MosseIfeestmettleraties.py',
              text: 'Download Deel 2',
              class: 'download-link',
              download: true
            }
          ]
        },
        {
          id: 7,
          title: 'BCS Butterfly Logo Ontwerp',
          description: 'Ik heb een modern en herkenbaar logo ontworpen voor BCS Butterfly, een lokaal Voedselfabrikant. Het logo moest zowel elegant als tijdloos zijn, met een subtiele verwijzing naar een vlinder (Butterfly) in het ontwerp. Na verschillende iteraties en feedbackrondes met de klant, is het eindresultaat een minimalistisch logo geworden dat goed werkt op zowel kleine als grote schaal. Het logo is geoptimaliseerd voor verschillende toepassingen, zoals visitekaartjes, verpakkingen en digitale media.',
          technologies: 'Adobe Photoshop, Canva, Figma',
          image: 'bcs.png',
        }
      ]
    }
  },
  methods: {
    selectCategory(category) {
      this.selectedCategory = category;
      window.scrollTo(0, 0);
    },
    hoverCategory(category) {
      this.hoverState = category;
    },
    resetHover() {
      this.hoverState = null;
    },
    goBack() {
      this.selectedCategory = null;
    },
    getImageUrl(imageName) {
      return `assets/images/${imageName}`;
    },
    getFileName(url) {
      return url.split('/').pop();
    },
    toggleView(view) {
      this.currentView = view;
    }
  }
}
</script>

<style>
.creaties-view {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  min-height: 100vh;
  padding-top: 80px; /* Added to prevent navbar overlap */
}

.title {
  text-align: center;
  margin-bottom: 3rem;
  font-size: 2.5rem;
  color: #333;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

.title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, #42b883, #347474);
  border-radius: 3px;
}

.categories-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.category-card {
  background: white;
  border-radius: 10px;
  padding: 2rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.category-card h2 {
  margin-bottom: 1rem;
  color: #2c3e50;
  position: relative;
  z-index: 2;
}

.category-card p {
  color: #7f8c8d;
  position: relative;
  z-index: 2;
}

.category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.hover-effect {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(66, 184, 131, 0.1), rgba(52, 116, 116, 0.1));
  opacity: 0;
  transition: opacity 0.3s ease;
}

.hover-effect.active {
  opacity: 1;
}

.category-card:nth-child(1):hover {
  border-top: 4px solid #42b883;
}

.category-card:nth-child(2):hover {
  border-top: 4px solid #3498db;
}

.category-card:nth-child(3):hover {
  border-top: 4px solid #9b59b6;
}

.projects-container {
  animation: fadeIn 0.5s ease;
  position: relative;
}

.back-button {
  background: #f8f9fa;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 2rem;
  transition: all 0.3s ease;
  position: sticky;
  top: 80px;
  z-index: 10;
}

.back-button:hover {
  background: #e9ecef;
  transform: translateX(-5px);
}

.section-title {
  text-align: center;
  margin-bottom: 3rem;
  font-size: 2rem;
  color: #2c3e50;
  position: relative;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 3px;
  background: linear-gradient(90deg, #42b883, #347474);
  border-radius: 3px;
}

.view-toggle {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.view-toggle button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  background: #f8f9fa;
  cursor: pointer;
  transition: all 0.3s ease;
}

.view-toggle button.active {
  background: #42b883;
  color: white;
}

.view-toggle button:hover {
  background: #e9ecef;
}

.view-toggle button.active:hover {
  background: #347474;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 2rem;
}

.project-card {
  background: white;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  opacity: 0;
  animation: fadeInUp 0.5s ease forwards;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.project-image {
  height: 200px;
  overflow: hidden;
}

.project-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.project-image img:hover {
  transform: scale(1.05);
}

.project-content {
  padding: 1.5rem;
}

.project-content h3 {
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.project-content p {
  color: #7f8c8d;
  margin-bottom: 1rem;
  line-height: 1.5;
}

.project-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}

.download-link, .demo-link {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  text-decoration: none;
  transition: all 0.3s ease;
  font-size: 0.9rem;
}

.download-link {
  background: #42b883;
  color: white;
}

.download-link:hover {
  background: #347474;
}

.demo-link {
  background: #3498db;
  color: white;
}

.demo-link:hover {
  background: #2980b9;
}

.projects-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.project-list-item {
  background: white;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  opacity: 0;
  animation: fadeInUp 0.5s ease forwards;
  padding: 1.5rem;
}

.project-list-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.list-item-content {
  display: flex;
  gap: 1.5rem;
}

.list-item-image {
  flex: 0 0 150px;
  height: 150px;
  border-radius: 5px;
  overflow: hidden;
}

.list-item-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.list-item-details {
  flex: 1;
}

.list-item-details h3 {
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.list-item-details p {
  color: #7f8c8d;
  margin-bottom: 0.5rem;
  line-height: 1.5;
}

.wpl2-case {
  background: white;
  border-radius: 10px;
  padding: 2rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  animation: fadeIn 0.5s ease;
}

.case-header {
  text-align: center;
  margin-bottom: 2rem;
}

.case-header h2 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.case-image {
  height: 300px;
  border-radius: 5px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.case-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.case-section {
  margin-bottom: 2rem;
}

.case-section h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
  position: relative;
  padding-bottom: 0.5rem;
}

.case-section h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 50px;
  height: 2px;
  background: #42b883;
}

.case-section p {
  color: #7f8c8d;
  line-height: 1.6;
}

.deliverables ul {
  list-style-type: none;
  padding-left: 0;
}

.deliverables ul li {
  padding: 0.5rem 0;
  color: #7f8c8d;
  position: relative;
  padding-left: 1.5rem;
}

.deliverables ul li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #42b883;
}

.deliverable-links {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

.deliverable-link {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background: #42b883;
  color: white;
  border-radius: 5px;
  text-decoration: none;
  transition: all 0.3s ease;
}

.deliverable-link:hover {
  background: #347474;
  transform: translateY(-2px);
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .categories-container {
    grid-template-columns: 1fr;
  }

  .projects-grid {
    grid-template-columns: 1fr;
  }

  .list-item-content {
    flex-direction: column;
  }

  .list-item-image {
    flex: 0 0 auto;
    width: 100%;
    height: 200px;
  }

  .project-links {
    flex-direction: column;
  }

  .download-link, .demo-link {
    width: 100%;
    text-align: center;
  }

  .deliverable-links {
    flex-direction: column;
  }
}
</style>
