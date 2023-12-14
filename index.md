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
        <div class="col-auto">
            CV<br><a href="/attachments/cv/cv.pdf">PDF File</a>
        </div>
    </div>
</div>

# About Me

I am an undergraduate student of [ACM Honors Class](https://acm.sjtu.edu.cn/), [Zhiyuan College](https://en.zhiyuan.sjtu.edu.cn/), [Shanghai Jiao Tong University](https://en.sjtu.edu.cn/), majoring in Computer Science and Technology.

Currently, I'm working as a research intern at [DSL](https://dsl.cis.upenn.edu/), [University of Pennsylvania](https://www.upenn.edu/), mentored by [Prof. Vincent Liu](https://vincen.tl/) and [Liangcheng Yu](https://liangchengyu.com/). We are doing research about FPGA-based SmartNIC.

My research interest lies in the fields of **systems, networking, and machine learning**. I am particularly drawn to a bottom-up research approach, beginning from the behavior of hardware such as FPGA and PCIe to intermediate layers like operating system and compiler, and extending up to applications like machine learning. This holistic way of thinking about the systems would open the door to identifying performance gaps between different layers and making optimizations with inventive system designs. Along this line, I am broadly interested in various problems in emerging networking and machine learning systems, including SmartNIC, FPGA, and distributed inference of LLM. I am also open to various topics in the broader field of systems, from serverless to databases. Recently, I'm working on improving network performance by offloading with FPGA-based SmartNICs.

> This page was updated in December 2023.

<div class="invisible-space" style="height: 3em"></div>

{% include_relative cv.md %}

<div class="invisible-space" style="height: 20vh"></div>

# More than coding

I've always been passionate about learning new knowledge from science and engineering to humanities and arts, and different cultures all around the world. I especially like music (.g. J-pop, symphony), graphic design (e.g. poster, font), animation, game as art, and different beverages (e.g. soda, cocktail).

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
