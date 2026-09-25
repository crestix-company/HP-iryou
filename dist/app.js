document.documentElement.classList.add('js');
const toggle=document.querySelector('.menu-toggle'),nav=document.querySelector('.nav');
if(toggle&&nav){const close=()=>{nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','メニューを開く');toggle.textContent='☰'};toggle.addEventListener('click',()=>{const opened=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(opened));toggle.setAttribute('aria-label',opened?'メニューを閉じる':'メニューを開く');toggle.textContent=opened?'×':'☰'});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){close();toggle.focus()}});window.matchMedia('(min-width:801px)').addEventListener('change',close)}
const elements=document.querySelectorAll('.reveal');
if('IntersectionObserver' in window){const obs=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target)}}),{threshold:.08});elements.forEach(e=>obs.observe(e));}else{elements.forEach(e=>e.classList.add('visible'))}

// Keep decorative motion running only while its section is visible.
const motionSections=document.querySelectorAll('.hero,.ai-wire,.development-map');
const sectionVisibility=new Map(Array.from(motionSections,element=>[element,true]));
const syncSectionMotion=()=>sectionVisibility.forEach((visible,element)=>element.classList.toggle('motion-paused',!visible||document.hidden));
if('IntersectionObserver' in window){
  const motionObserver=new IntersectionObserver(entries=>{
    entries.forEach(entry=>sectionVisibility.set(entry.target,entry.isIntersecting));
    syncSectionMotion();
  },{threshold:0});
  motionSections.forEach(element=>motionObserver.observe(element));
}
document.addEventListener('visibilitychange',syncSectionMotion);
syncSectionMotion();
