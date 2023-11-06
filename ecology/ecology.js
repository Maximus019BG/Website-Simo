function changeColor() {
        var x = document.getElementById("gfg");
        var y = document.getElementById("gfg1");
        var z = document.getElementById("gfg2");
        var u = document.getElementById("gfg3");
        var i = document.getElementById("gfg4");
        var o = document.getElementById("gfg5");
      
        x.style.color = "black";
        y.style.color = "black";
        z.style.color = "black";
        u.style.color = "black";
        i.style.color = "black";
        o.style.color = "black";

      }

      window.onscroll = () => {
        const nav = document.querySelector('#navbar');
        if(this.scrollY <= 10) nav.className = ''; else nav.className = 'scroll';
      
        
        changeColor();
        
      };
      
/////


document.querySelector(".search-btn").addEventListener("click", ()=>{

    search = document.querySelector(".search").value
  
           if(search%2==0){ console.log("⚠️Warning: This search engine is not connected to the website ❗️")
                            alert("⚠️  This search engine is not connected to the website ❗️") 
           }
           if(search%2===1){ console.log("⚠️Warning: This search engine is not connected to the website ❗")
                             alert("⚠️  This search engine is not connected to the website ❗️") 
           }
  
  
  
  
  
  //   +++ Qidiruv tarixiga qo'shilgan web saytlar +++
  
  
  
  
  
  // ===Qisqartirilmagan holat===
  
          else if(search==='kun.uz'){ location = "https://kun.uz/"
  
          }
  
          else if(search==='youtube.com'){ location = "https://www.youtube.com/"
  
          }
  
          else if(search==='telegram.org'){ location = "https://web.telegram.org/a/"
  
          }
  
          else if(search==='canva.com'){ location = "https://canva.com/"
  
          }
  
          else if(search==='fontawesome.com'){ location = "https://fontawesome.com/"
  
          }
  
          else if(search==='discord.com'){ location = "https://discord.com/"
  
          }
  
          else if(search==='panzoid.com'){ location = "https://panzoid.com/"
  
          }
  
          else if(search==='upg.uz'){ location = "https://upg.uz/"
  
          }
  
          else if(search==='youtube.channel/TOMS LIDER'){ location = "https://www.youtube.com/@TOMS_LIDER"
  
          }
  
          else if(search==='live server'){ location = "http://127.0.0.1:5500/"
  
          }
  
  // ===Finsh===
  
  
  
  
  
  
  
  // ---Qisqartirilgan holat---
  
          else if(search==='kun'){ location = "https://kun.uz/"
  
          }
  
          else if(search==='yt'){ location = "https://www.youtube.com/"
  
          }
  
          else if(search==='tg'){ location = "https://web.telegram.org/a/"
  
          }
  
          else if(search==='cv'){ location = "https://canva.com/"
  
          }
  
          else if(search==='fa'){ location = "https://fontawesome.com/"
  
          }
  
          else if(search==='dd'){ location = "https://discord.com/"
  
          }
  
          else if(search==='pd'){ location = "https://panzoid.com/"
  
          }
  
          else if(search==='upg'){ location = "https://upg.uz/"
  
          }
  
          else if(search==='yt.TL'){ location = "https://www.youtube.com/@TOMS_LIDER"
  
          }
  
          else if(search==='ls'){ location = "http://127.0.0.1:5500/"
  
          }
  
  // ---Finsh---
  
  
  
  
  
  // +++ Finsh all URL +++
  
  
  
  
  
  
  
  
  document.querySelector(".search").value = ""
  
  })
  
  
  
  
  // CARDS
  
  