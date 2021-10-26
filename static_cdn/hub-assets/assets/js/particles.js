$(window).on("load", function() {
    $("#particles-js").length && particlesJS("particles-js", {
        particles: {
            number: {
                value: 28
            },
            color: {
                value: ["#0182cc", "#00befa", "#0182cc"]
            },
            shape: {
                type: "circle"
            },
            opacity: {
                value: 1,
                random: !1,
                anim: {
                    enable: !1
                }
            },
            size: {
                value: 3,
                random: !0,
                anim: {
                    enable: !1
                }
            },
            line_linked: {
                enable: !1
            },
            move: {
                enable: !0,
                speed: 2,
                direction: "none",
                random: !0,
                straight: !1,
                out_mode: "out"
            }
        },
        interactivity: {
            detect_on: "canvas",
            events: {
                onhover: {
                    enable: !1
                },
                onclick: {
                    enable: !1
                },
                resize: !0
            }
        },
        retina_detect: !0
    })
});