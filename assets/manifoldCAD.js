import"./modulepreload-polyfill.js";function ne(){return new Worker("/assets/worker-wrapper-fdf3b278.js",{type:"module"})}const T="<code>",y=self.examples.functionBodies;navigator.serviceWorker&&navigator.serviceWorker.register("/service-worker.js",{scope:"./index.html"});let l;const oe=document.querySelector("#undo"),le=document.querySelector("#redo"),ce=document.querySelector("#format"),ie=document.querySelector("#share");oe.onclick=()=>l.trigger("ignored","undo");le.onclick=()=>l.trigger("ignored","redo");ce.onclick=()=>l.trigger("ignored","editor.action.formatDocument");ie.onclick=()=>{const e=new URL(window.location.toString());e.hash="#"+encodeURIComponent(m.textContent+T+l.getValue()),navigator.clipboard.writeText(e.toString()),console.log("Shareable link copied to clipboard!"),console.log("Consider shortening this URL using tinyURL.com")};const re=document.querySelector("#file"),m=document.querySelector("#current"),H=document.querySelector("#file .uparrow"),I=document.querySelector("#fileDropdown"),$=document.querySelector("#save"),h=document.querySelector("#saveDropdown"),E=document.querySelector("#save .uparrow"),se=function(){I.classList.remove("show"),h.classList.remove("show"),H.classList.remove("down"),E.classList.remove("down")},ae=function(e){e.stopPropagation(),I.classList.toggle("show"),H.classList.toggle("down")},ue=function(e){e.stopPropagation(),h.classList.toggle("show"),E.classList.toggle("down")};re.onclick=ae;E.parentElement.onclick=ue;document.body.onclick=se;const C="ManifoldCAD";function L(e){return window.localStorage.getItem(C+e)}function g(e,n){window.localStorage.setItem(C+e,n)}function z(e){window.localStorage.removeItem(C+e)}function de(e){if(e>=window.localStorage.length)return;const n=window.localStorage.key(e);if(n.startsWith(C))return n.slice(C.length)}function R(){if(l){const e=m.textContent;y.get(e)||g(e,l.getValue())}}window.onpagehide=R;window.beforeunload=R;let q=!1,U=!0;function w(e){if(l){q=!0,m.textContent=e,g("currentName",e),U=y.get(e)!=null;const n=U?y.get(e).substring(1):L(e)??"";window.location.hash="#"+e,l.setValue(n)}}function D(e){const n=document.createElement("div");n.classList.add("item");const t=document.createElement("button");n.appendChild(t),t.type="button",t.classList.add("blue","item");const o=document.createElement("span");return t.appendChild(o),o.textContent=e,t.onclick=function(){R(),w(o.textContent)},t.onkeyup=function(c){c.preventDefault()},t}function N(e){const n=document.createElement("button");return n.classList.add("icon"),e.parentElement.appendChild(n),n}function K(e){let n=1,t=e;for(;L(t)!=null||y.get(t)!=null;)t=e+" "+n++;return t}function _(e){const n=e.firstChild,t=N(e);t.classList.add("edit"),t.onclick=function(f){f.stopPropagation();const s=n.textContent,ee=L(s),v=document.createElement("form"),a=document.createElement("input");a.classList.add("name"),a.value=s,n.textContent="",e.appendChild(v),v.appendChild(a),a.focus(),a.setSelectionRange(0,s.length);function te(){const S=a.value;if(a.blur(),!S)return;const M=K(S);n.textContent=M,m.textContent==s&&(m.textContent=M),z(s),g(M,ee)}v.onsubmit=te,a.onclick=function(S){S.stopPropagation()},a.onblur=function(){e.removeChild(v),n.textContent=s}};const o=N(e);o.classList.add("trash");let c=0;o.onclick=function(f){if(f.stopPropagation(),e.classList.contains("blue"))c=performance.now(),e.classList.remove("blue"),e.classList.add("red"),document.body.addEventListener("click",function(){e.classList.add("blue"),e.classList.remove("red")},{once:!0});else if(performance.now()-c>500){z(n.textContent),m.textContent==n.textContent&&w("Intro");const s=e.parentElement;s.parentElement.removeChild(s)}}}const W=document.querySelector("#new");function B(e,n=void 0){const t=K(n??"New Script");g(t,e);const o=D(t);return W.insertAdjacentElement("afterend",o.parentElement),_(o),{button:o,name:t}}W.onclick=function(){B("").button.click()};const r=document.querySelector("#compile"),G=document.querySelector("#poster");let A=!1,x=!0;function J(){r.disabled=!1,x?r.click():G.textContent="Auto-run disabled"}let j;async function fe(){const e=await fetch("/manifold-global-types.d.ts").then(t=>t.text()),n=await fetch("/manifold-encapsulated-types.d.ts").then(t=>t.text());return`
${e.replaceAll("export","")}
${n.replace(/^import.*$/gm,"").replaceAll("export","declare")}
declare interface ManifoldToplevel {
  CrossSection: typeof T.CrossSection;
  Manifold: typeof T.Manifold;
  Mesh: typeof T.Mesh;
  triangulate: typeof T.triangulate;
  setMinCircularAngle: typeof T.setMinCircularAngle;
  setMinCircularEdgeLength: typeof T.setMinCircularEdgeLength;
  setCircularSegments: typeof T.setCircularSegments;
  getCircularSegments: typeof T.getCircularSegments;
  resetToCircularDefaults: typeof T.resetToCircularDefaults;
  setup: () => void;
}
declare const module: ManifoldToplevel;
`}async function me(){return`${(await fetch("/editor.d.ts").then(n=>n.text())).replace(/^import.*$/gm,"")}`}require.config({paths:{vs:"https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.34.0/min/vs"}});require(["vs/editor/editor.main"],async function(){monaco.languages.typescript.typescriptDefaults.addExtraLib(await fe()),monaco.languages.typescript.typescriptDefaults.addExtraLib(await me()),l=monaco.editor.create(document.getElementById("editor"),{language:"typescript",automaticLayout:!0}),j=await(await monaco.languages.typescript.getTypeScriptWorker())(l.getModel().uri),l.getModel().updateOptions({tabSize:2});for(const[t]of y){const o=D(t);I.appendChild(o.parentElement)}let n=m.textContent;for(let t=0;t<window.localStorage.length;t++){const o=de(t);if(o)if(o==="currentName")n=L(o);else if(o==="safe")x=L(o)!=="false";else{const c=D(o);W.insertAdjacentElement("afterend",c.parentElement),_(c)}}if(window.location.hash.length>0){const t=decodeURIComponent(window.location.hash.substring(1)),o=t.indexOf(T);if(o!=-1){x=!0;const c=t.substring(0,o);w(B(t.substring(o+T.length),c).name)}else t!=n&&(x=!0),w(t)}else w(n);A&&J(),l.onDidChangeModelContent(t=>{if(r.disabled=!1,q){q=!1,l.setScrollTop(0);return}if(U){const o=l.getPosition();B(l.getValue()).button.click(),l.setPosition(o)}}),window.onresize=()=>{l.layout({})}});const u=document.querySelector("model-viewer"),pe=document.querySelector("#animation"),b=document.querySelector("#play"),p=document.querySelector("#scrubber");let P=!1;u.addEventListener("load",()=>{const e=u.availableAnimations.length>0;pe.style.display=e?"flex":"none",e&&Q()});function Q(){u.play(),b.classList.remove("play"),b.classList.add("pause"),P=!1,p.classList.add("hide")}function ge(){u.pause(),b.classList.remove("pause"),b.classList.add("play"),P=!0,p.max=u.duration,p.value=u.currentTime,p.classList.remove("hide")}b.onclick=function(){P?Q():ge()};p.oninput=function(){u.currentTime=p.value};const d=document.querySelector("#console"),he=console.log;console.log=function(e){d.textContent+=e+`\r
`,d.scrollTop=d.scrollHeight,he(e)};function we(){d.textContent=""}function ye(){r.firstChild.style.visibility="hidden",r.classList.add("red","cancel")}function Ce(){r.firstChild.style.visibility="visible",r.classList.remove("red","cancel")}let X=performance.now();function Y(){Ce();const e=performance.now(),n=d.textContent;d.textContent=n.substring(n.indexOf(`
`)+1),console.log(`Took ${(Math.round((e-X)/10)/100).toLocaleString()} seconds`)}const i={glbURL:null,threeMFURL:null};let k=null;function O(){k=new ne,k.onmessage=function(e){if(e.data==null){j!=null&&!A&&J(),A=!0;return}if(e.data.log!=null){d.textContent+=e.data.log+`\r
`,d.scrollTop=d.scrollHeight;return}Y(),r.disabled=!0,i.threeMFURL!=null&&(URL.revokeObjectURL(i.threeMFURL),i.threeMFURL=null),URL.revokeObjectURL(i.glbURL),i.glbURL=e.data.glbURL,i.threeMFURL=e.data.threeMFURL,F.disabled=i.threeMFURL==null,u.src=i.glbURL,i.glbURL==null?(u.showPoster(),G.textContent="Error",O()):g("safe","true")}}O();async function Le(){R(),g("safe","false"),ye(),we(),console.log("Running...");const e=await j.getEmitOutput(l.getModel().uri.toString());k.postMessage(e.outputFiles[0].text),X=performance.now()}function be(){k.terminate(),O(),Y(),console.log("Run canceled")}r.onclick=function(){r.classList.contains("cancel")?be():Le()};function Z(e,n,t){const o=e.parentElement;return()=>{const c=$.firstElementChild;c!==o&&(h.insertBefore(c,h.firstElementChild),$.insertBefore(o,h),o.appendChild(E.parentElement));const f=document.createElement("a");f.download=n,f.href=i[t],f.click()}}const V=document.querySelector("#glb");V.onclick=Z(V,"manifold.glb","glbURL");const F=document.querySelector("#threemf");F.onclick=Z(F,"manifold.3mf","threeMFURL");
//# sourceMappingURL=manifoldCAD.js.map
