<template>
  <div class="contact-view">
    <div class="header">
      <h1>Contact</h1>
    </div>

    <transition name="fade" appear>
      <div class="section availability">
        <h2 class="section-title">Beschikbaarheid voor contact</h2>
        <div class="availability-grid">
          <div v-for="(day, index) in availability" :key="day.name" class="day-item" :style="{ 'transition-delay': `${index * 0.1}s` }">
            <span class="day-name">{{ day.name }}:</span>
            <span class="day-time">{{ day.time }}</span>
          </div>
        </div>
      </div>
    </transition>

    <transition name="slide" appear>
      <div class="section personal-info">
        <h2 class="section-title">Persoonlijke Informatie</h2>
        <div class="info-grid">
          <div v-for="(info, index) in personalInfo" :key="info.label" class="info-item" :style="{ 'transition-delay': `${index * 0.1}s` }">
            <span class="info-label">{{ info.label }}:</span>
            <span class="info-value">{{ info.value }}</span>
          </div>
        </div>
      </div>
    </transition>

    <transition name="fade" appear>
      <div class="section contact-info">
        <h2 class="section-title">Contactgegevens</h2>
        <div class="contact-methods">
          <div v-for="(method, index) in contactMethods" :key="method.type" class="contact-method" :style="{ 'transition-delay': `${index * 0.15}s` }">
            <div class="contact-icon">
              <i :class="method.icon"></i>
            </div>
            <div class="contact-details">
              <span class="contact-type">{{ method.type }}</span>
              <a v-if="method.link" :href="method.link" class="contact-value">{{ method.value }}</a>
              <span v-else class="contact-value">{{ method.value }}</span>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <transition name="bounce" appear>
      <div class="cta">
        <p>Neem gerust contact met me op!</p>
        <button class="contact-btn" @click="sendEmail">Stuur een bericht</button>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'ContactView',
  data() {
    return {
      availability: [
        { name: 'Maandag', time: 'Niet beschikbaar' },
        { name: 'Dinsdag', time: '17:00 - 20:00 uur' },
        { name: 'Woensdag', time: '17:00 - 20:00 uur' },
        { name: 'Donderdag', time: 'Niet beschikbaar' },
        { name: 'Vrijdag', time: '10:00 - 17:00 uur' },
        { name: 'Zaterdag', time: '9:00 - 20:00 uur' },
        { name: 'Zondag', time: '9:00 - 20:00 uur' }
      ],
      personalInfo: [
        { label: 'Naam', value: 'Alperen Ozcelik' },
        { label: 'Leeftijd', value: '22 jaar' },
        { label: 'Woonplaats', value: '3550, Heusden-Zolder' }
      ],
      contactMethods: [
        { type: 'School E-mail', value: '12402378@student.pxl.be', icon: 'fas fa-envelope', link: 'mailto:12402378@student.pxl.be' },
        { type: 'Persoonlijk E-mail', value: 'Alp123oz@outlook.com', icon: 'fas fa-envelope-open', link: 'mailto:Alp123oz@outlook.com' },
        { type: 'Telefoonnummer', value: '+32 487 10 09 87', icon: 'fas fa-phone-alt', link: 'tel:+32487100987' }
      ]
    }
  },
  methods: {
    sendEmail() {
      window.location.href = 'mailto:Alp123oz@outlook.com'
    }
  }
}
</script>

<style scoped>
.contact-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  color: #333;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.header {
  text-align: center;
  margin-bottom: 3rem;
}

.header h1 {
  font-size: 3rem;
  color: #2c3e50;
  position: relative;
  display: inline-block;
}

.header h1::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 4px;
  background: linear-gradient(to right, #3498db, #2ecc71);
  border-radius: 2px;
}

.section {
  background: white;
  border-radius: 10px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.section-title {
  color: #2c3e50;
  margin-top: 0;
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #f1f1f1;
  font-size: 1.5rem;
}

.availability-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.day-item {
  padding: 0.8rem;
  background: #f8f9fa;
  border-radius: 5px;
  transform: translateY(20px);
  opacity: 0;
  animation: slideUp 0.5s forwards;
}

.day-name {
  font-weight: bold;
  display: block;
  color: #3498db;
}

.day-time {
  color: #7f8c8d;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.info-item {
  padding: 0.8rem;
  background: #f8f9fa;
  border-radius: 5px;
  transform: translateX(-20px);
  opacity: 0;
  animation: slideRight 0.5s forwards;
}

.info-label {
  font-weight: bold;
  display: block;
  color: #3498db;
}

.info-value {
  color: #7f8c8d;
}

.contact-methods {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.contact-method {
  display: flex;
  align-items: center;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 5px;
  transform: scale(0.9);
  opacity: 0;
  animation: scaleIn 0.5s forwards;
}

.contact-icon {
  margin-right: 1rem;
  font-size: 1.5rem;
  color: #3498db;
}

.contact-details {
  display: flex;
  flex-direction: column;
}

.contact-type {
  font-weight: bold;
  color: #2c3e50;
}

.contact-value {
  color: #7f8c8d;
  text-decoration: none;
}

.contact-value:hover {
  color: #3498db;
  text-decoration: underline;
}

.cta {
  text-align: center;
  margin-top: 2rem;
  opacity: 0;
  animation: fadeIn 1s forwards 0.5s;
}

.contact-btn {
  background: linear-gradient(to right, #3498db, #2ecc71);
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 50px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
}

.contact-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4);
}

.contact-btn:active {
  transform: translateY(1px);
}

/* Animations */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.8s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.slide-enter-active {
  transition: all 0.5s ease;
}
.slide-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.bounce-enter-active {
  animation: bounce-in 0.8s;
}

@keyframes slideUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideRight {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes scaleIn {
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

@keyframes bounce-in {
  0% {
    transform: scale(0.9);
    opacity: 0;
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}
</style>
