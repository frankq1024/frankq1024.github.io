---
layout: home
title: Home
---

<h1 style="font-family: var(--type-serif-cn); margin-top: 1em">仇天元</h1>

> The pronunciation of my Chinese name is "Chyoh Tyen Ywen" (Qíu Tiān Yuán).

<style>
  .no-padding-here {
    padding: 0 !important;
  }
</style>

<div class="container no-padding-here" style="padding-left: 0em; padding-right: 0em; margin-top: 2em">
    <div class="row justify-content-between align-items-center no-padding-here">
        <div class="col-auto">
            GitHub<br><a href="https://github.com/{{ site.social.github }}">{{ site.social.github }}</a>
        </div>
        <div class="col-auto">
            LinkedIn<br><a href="https://www.linkedin.com/in/{{ site.social.linkedin }}">{{ site.social.linkedin }}</a>
        </div>
        <div class="col-auto">
            E-mail<br><a href="mailto:{{ site.social.email }}">{{ site.social.email }}</a>
        </div>
    </div>
</div>

# About Me

I am an undergraduate student at the [ACM Honors Class](https://acm.sjtu.edu.cn/) of [Zhiyuan College](https://en.zhiyuan.sjtu.edu.cn/), [Shanghai Jiao Tong University](https://en.sjtu.edu.cn/), majoring in Computer Science and Technology. I will be a PhD student in [Purdue University](https://www.purdue.edu/) [Electrical and Computer Engineering](https://engineering.purdue.edu/ECE) department, mentored by [Prof. Xiaoqi Chen](https://engineering.purdue.edu/~xiaoqic/).

My research interest lies in the fields of **systems and networking**. I am particularly drawn to a bottom-up research approach, beginning from the behavior of hardware such as FPGA and PCIe to intermediate layers like operating system, and extending up to applications. This holistic way of thinking about the systems would open the door to identifying performance gaps between different layers and making optimizations with inventive system designs. Along this line, I am broadly interested in various problems in emerging networking and systems, including SmartNIC, FPGA. I am also open to various topics in the broader field of systems, from serverless to databases. Recently, I'm working on improving network performance by offloading with FPGA-based SmartNICs.

> This page was updated in February 2024.

<div class="invisible-space" style="height: 3em"></div>

{% include_relative cv.md %}

<div class="invisible-space" style="height: 20vh"></div>

# More than coding

My life’s ambition is to make the world a better place.

For my hobbies, I've always been passionate about learning new knowledge from science and engineering to humanities and arts, and different cultures all around the world. I especially like music (e.g. J-pop, symphony), graphic design (e.g. poster, font), animation, game as art, and different beverages (e.g. soda, cocktail).

Here is a simple work written in Processing many years ago.

<div class="invisible-space" style="height: 15vh"></div>

<div id="bulkyContainer" style="position: relative; width: 100vw; height: 10vh; left: 50%; transform: translateX(-50%);">
  <div id="clickToLoad" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); cursor: pointer;">
    Click to Load
  </div>
  <div id="iframeContainer" style="display: none;">
    <iframe id="iframe" src="" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"></iframe>
  </div>
</div>

<script>
    var bulkyContainer = document.getElementById("bulkyContainer");
    var clickToLoad = document.getElementById("clickToLoad");
    var iframeContainer = document.getElementById("iframeContainer");
    var iframe = document.getElementById("iframe");

    clickToLoad.addEventListener("click", function() {
        bulkyContainer.style.height = "100vh";
        clickToLoad.style.display = "none";
        iframeContainer.style.display = "block";
        iframe.src = "https://openprocessing.org/sketch/2080432/embed/";
        bulkyContainer.scrollIntoView({ behavior: 'smooth' }); // Smooth scroll to the top of the bulkyContainer element
    });
</script>


<div class="invisible-space" style="height: 40vh"></div>

<!--{% include archive.html %}-->
