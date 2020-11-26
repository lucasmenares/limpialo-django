var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/css/estilos.css',
    '/static/images/logo-blanco.png',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })

      })
      .catch(function(e){
          return caches.match(event.request)
      })
    );
});


///////////////////////////////
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');
	// Your web app's Firebase configuration
	var firebaseConfig = {
		apiKey: "AIzaSyBSOfHtgj7hlgV73ssxNlbjglB0GG79mmI",
		authDomain: "limpialo-django.firebaseapp.com",
		databaseURL: "https://limpialo-django.firebaseio.com",
		projectId: "limpialo-django",
		storageBucket: "limpialo-django.appspot.com",
		messagingSenderId: "375186697608",
		appId: "1:375186697608:web:44c78ea247997b57b35e3d"
	};
	// Initialize Firebase
	firebase.initializeApp(firebaseConfig);
	//////////////////////////////////////////
	let messaging = firebase.messaging()

  messaging.setBackgroundMessageHandler(function(payload) {
    let titulo = payload.notification.title
    let opciones = {
        body: payload.notification.body,
        icon: payload.notification.icon
    }
    self.registration.showNotification(titulo, opciones)
})
