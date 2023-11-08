---
layout: home
title: Home
---

# Tianyuan Qiu (仇天元)

<style>
  .no-padding-here {
    padding: 0 !important;
  }
</style>

<div class="container no-padding-here" style="padding-left: 0em; padding-right: 0em; margin-top: 2em">
    <div class="row justify-content-between align-items-center no-padding-here">
        <div class="col-auto">
            Github<br><a href="https://github.com/{{ site.social.github }}">{{ site.social.github }}</a>
        </div>
        <div class="col-auto">
            Linkdein<br><a href="https://www.linkedin.com/in/{{ site.social.linkedin }}">{{ site.social.linkedin }}</a>
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

Currently, I'm working as a research intern at [DSL](https://dsl.cis.upenn.edu/), [University of Pennsylvania](https://www.upenn.edu/), mentored by [Prof. Vincent Liu](https://vincen.tl/) and [Ph.D. Liangcheng Yu](https://liangchengyu.com/). We are doing research about FPGA-based SmartNIC.

> This page was updated in November 2023

<div class="invisible-space" style="height: 3em"></div>

{% include_relative cv.md %}

<div class="invisible-space" style="height: 20vh"></div>

# More than coding

I've always been passionate about learning new knowledge, whether it's in the realm of science and engineering or in humanities and the arts.

<div class="invisible-space" style="height: 15vh"></div>

<div id="container" style="position: relative; width: 100vw; height: 100vh; left: 50%; transform: translateX(-50%);">
  <div id="clickToLoad" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); cursor: pointer;">
    Click to load
  </div>
  <div id="iframeContainer" style="display: none;">
    <iframe id="iframe" src="" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"></iframe>
  </div>
</div>

<script>
  var clickToLoad = document.getElementById("clickToLoad");
  var iframeContainer = document.getElementById("iframeContainer");
  var iframe = document.getElementById("iframe");

  clickToLoad.addEventListener("click", function() {
    clickToLoad.style.display = "none";
    iframeContainer.style.display = "block";
    iframe.src = "https://openprocessing.org/sketch/2080432/embed/";
  });
</script>


<div class="invisible-space" style="height: 40vh"></div>

<!--{% include archive.html %}-->
