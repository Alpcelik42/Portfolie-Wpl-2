<template>
  <footer class="footer">
    <div class="footer__container">
      <!-- Contact Sectie -->
      <div class="footer__contact">
        <h3 class="footer__title">Neem Contact Op</h3>
        <p class="footer__text">Aarzel niet om me te benaderen – ik hoor graag van je!</p>

        <div class="footer__buttons">
          <a
            href="mailto:alp123oz@outlook.com"
            class="footer__button footer__button--email"
          >
            <span class="footer__button-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                <path d="M1.5 8.67v8.58a3 3 0 003 3h15a3 3 0 003-3V8.67l-8.928 5.493a3 3 0 01-3.144 0L1.5 8.67z" />
                <path d="M22.5 6.908V6.75a3 3 0 00-3-3h-15a3 3 0 00-3 3v.158l9.714 5.978a1.5 1.5 0 001.572 0L22.5 6.908z" />
              </svg>
            </span>
            <span>alp123oz@outlook.com</span>
          </a>

          <button
            @click="openPrivacyPolicy"
            class="footer__button footer__button--privacy"
          >
            <span class="footer__button-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                <path fill-rule="evenodd" d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z" clip-rule="evenodd" />
              </svg>
            </span>
            <span>Privacybeleid</span>
          </button>
        </div>
      </div>

      <!-- Copyright en Social Media -->
      <div class="footer__bottom">
        <div class="footer__social">
          <a href="https://www.linkedin.com/in/alperen-ozcelik-28a878331/" class="footer__social-link" aria-label="LinkedIn">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-11h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-5.5c0-1.33-.05-3-1.5-3s-1.93 1.67-2 3v5.5h-3v-11h3v1.5a3.6 3.6 0 013.2-1.5c2.36 0 4 1.49 4 4.5z"/>
            </svg>
          </a>
          <a href="https://github.com/Alpcelik42" class="footer__social-link" aria-label="GitHub">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 .5C5.37.5 0 5.78 0 12.29c0 5.15 3.438 9.56 8.205 11.1.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.23-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57C20.565 21.85 24 17.44 24 12.29c0-6.51-5.37-11.79-12-11.79z"/>
            </svg>
          </a>
        </div>

        <p class="footer__copyright">
          &copy; {{ new Date().getFullYear() }} Alperen Ozcelik. Alle rechten voorbehouden.
        </p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterComponent',
  methods: {
    openPrivacyPolicy() {
      // Direct link naar het Privacybeleid.txt bestand in de root
      window.open('/Privacybeleid.txt', '_blank');
    }
  }
}
</script>

<style scoped>
/* Basis stijlen */
.footer {
  background-color: #2c3e50;
  color: #ecf0f1;
  padding: 50px 0 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.footer__container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Contact sectie */
.footer__contact {
  text-align: center;
  margin-bottom: 40px;
}

.footer__title {
  font-size: 1.8rem;
  margin-bottom: 15px;
  color: #3498db;
}

.footer__text {
  font-size: 1.1rem;
  max-width: 600px;
  margin: 0 auto 30px;
  line-height: 1.6;
}

.footer__buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.footer__button {
  display: inline-flex;
  align-items: center;
  padding: 12px 25px;
  border-radius: 50px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
  cursor: pointer;
  border: none;
  font-size: 1rem;
}

.footer__button-icon {
  display: inline-flex;
  margin-right: 10px;
  width: 20px;
  height: 20px;
}

.footer__button-icon svg {
  width: 100%;
  height: 100%;
}

.footer__button--email {
  background-color: #3498db;
  color: white;
}

.footer__button--email:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.footer__button--privacy {
  background-color: #2ecc71;
  color: white;
}

.footer__button--privacy:hover {
  background-color: #27ae60;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Onderste sectie */
.footer__bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.footer__social {
  display: flex;
  gap: 20px;
  margin-bottom: 15px;
}

.footer__social-link {
  color: #ecf0f1;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  background-color: rgba(255, 255, 255, 0.1);
}

.footer__social-link:hover {
  background-color: #3498db;
  transform: translateY(-3px);
}

.footer__social-link svg {
  width: 20px;
  height: 20px;
}

.footer__copyright {
  font-size: 0.9rem;
  opacity: 0.8;
  text-align: center;
}

/* Responsieve aanpassingen */
@media (max-width: 768px) {
  .footer__buttons {
    flex-direction: column;
    align-items: center;
  }

  .footer__button {
    width: 100%;
    max-width: 250px;
    justify-content: center;
  }

  .footer__title {
    font-size: 1.5rem;
  }

  .footer__text {
    font-size: 1rem;
  }
}
</style>
