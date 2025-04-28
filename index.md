---
layout: home
title: Home
---

<h1 style="font-family: var(--type-serif-cn); margin-top: 1em">仇天元</h1>

> The pronunciation of my Chinese name is "Chyoh Tyen Ywen" (Mandarin Pinyin: Qíu Tiān Yuán).

<style>
  .no-padding-here {
    padding: 0 !important;
  }
</style>

<div class="container no-padding-here" style="padding-left: 0em; padding-right: 0em; margin-top: 2em">
    <div class="row justify-content-between align-items-center no-padding-here">
        <div class="col-auto">
            GitHub<br>
            <a href="https://github.com/{{ site.social.github }}">{{ site.social.github }}</a>
        </div>
        <div class="col-auto">
            LinkedIn<br>
            <a href="https://www.linkedin.com/in/{{ site.social.linkedin }}">{{ site.social.linkedin }}</a>
        </div>
        <div class="col-auto">
            E-mail<br>
            <a href="mailto:{{ site.social.email }}">{{ site.social.email }}</a>
        </div>
        <div class="col-auto">
            Resume<br>
            <a href="/attachments/resume.pdf" target="_blank">PDF</a>
        </div>
    </div>
</div>

# About Me

I am currently a Ph.D. student in [ECE](https://engineering.purdue.edu/ECE) ([PurNET Lab](https://purnet-lab.gitlab.io/)) at [Purdue University](https://www.purdue.edu/), advised by [Prof. Xiaoqi Chen](https://engineering.purdue.edu/~xiaoqic/), with a focus on research in computer networking systems.

My research interests span **systems, networking, and machine learning**. I am particularly drawn to a bottom-up research approach that starts from the behavior of hardware components such as FPGAs and PCIe, extends through intermediate layers like operating systems and compilers, and reaches applications like machine learning. This holistic perspective enables me to identify performance gaps between layers and explore optimizations through innovative system design. My work broadly covers emerging challenges in networking and machine learning system, including FPGA-based SmartNIC, GPU, and distributed training of LLM. I am also open to exploring a range of topics in the broader systems field, from serverless to database.

I earned my Bachelor's degree in CS (Zhiyuan Honors Program) from the [ACM Class](https://acm.sjtu.edu.cn/), [Zhiyuan College](https://en.zhiyuan.sjtu.edu.cn/), at [Shanghai Jiao Tong University](https://en.sjtu.edu.cn/). During my undergraduate, I interned as a research assistant of [DSL](https://dsl.cis.upenn.edu/) at the [University of Pennsylvania](https://www.upenn.edu/), where I was mentored by [Prof. Vincent Liu](https://vincen.tl/) and [Ph.D. Liangcheng Yu](https://liangchengyu.com/). Our research focused on FPGA-based SmartNICs and PCIe systems. Prior to that, I completed an internship as a research assistant in the field of computer vision under [Prof. Li Niu](https://www.ustcnewly.com/), working on diverse image harmonization.

> This page was updated in January 2025.

<div class="invisible-space" style="height: 3em"></div>

{% include_relative cv.md %}

<div class="invisible-space" style="height: 20vh"></div>

# More than coding

My life's ambition is to make the world a better place with more humanistic care.

For my hobbies, I've always been passionate about learning new knowledge from science and engineering to humanities and arts, and different cultures all around the world. I especially like music (e.g. J-pop, J-rock), graphic design (e.g. poster, font), animation, game as art, and different beverages (e.g. soda, whiskey, cocktail, coffee).

Since arriving in Indiana, I have chances to engage more in some localized hobbies, like karting, snowboarding, and figure skating! And I'm quite looking forward to a road trip around the entire country!

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
