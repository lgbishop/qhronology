.. Qhronology documentation master file, created by
   sphinx-quickstart on Thu Jan 01 00:00:00 1970.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: /styles.rst

.. raw:: html

   <!-- style>body .bd-header, .navbar {display: none; visibility: hidden;}</style -->
   <style>
      .bd-main .bd-content .bd-article-container .bd-article {
          padding-top: 0rem;
      }
   </style>

.. raw:: html

   <style>
      .bd-container {
         overflow: hidden;
      }

      .full-width {
         width: 100vw;
         position: relative;
         left: 50%;
         right: 50%;
         margin-left: -50vw;
         margin-right: -50vw;
      /*    padding-left: 0px; */
      /*    padding-right: 18px; */ /* For scrollbar. */ 
         overflow-x: visible !important;
         background-color: var(--pst-color-sd-bg-black) !important;
         -webkit-backdrop-filter: blur(2px);
         backdrop-filter: blur(2px);
         padding-top: 1rem;
      }

      .bd-main .bd-content .bd-article-container .bd-article {
         width: 100%;
         padding: 0rem;
         padding-top: 1.0rem;
         /* max-width: 120%; */
         /* overflow: visible !important; */
      }

      /* Width of the body content (including sidebars?), default is 60rem. */
      .bd-main .bd-content .bd-article-container {
         max-width: 120%;
         overflow: visible !important;
      }

      /* Padding between the content and the sidebars, header, and footer. */
      .bd-article-container {
         padding-top: 0rem !important;
         padding-bottom: 3rem !important;
         padding-left: 3rem !important;
         padding-right: 3rem !important;
      }

      .sd-bg-black {
         padding-left: calc(50vw - (88rem / 2));
      }

      .sd-bg-white {
         padding-right: calc(50vw - (88rem / 2)); /* + 20px); */
      }
   </style>

.. raw:: html

   <style>
      html[data-theme="dark"] .sd-bg-black, .sd-bg-white, .sd-bg-transparent {
         --pst-color-shadow: rgba(255,255,255,0.0) !important;
      }

      html[data-theme="light"] .sd-bg-black, .sd-bg-white, .sd-bg-transparent {
         --pst-color-shadow: rgba(255,255,255,0.0) !important;
      }
   </style>

.. .. raw:: html

..    <style>
..      .sd-col-8 {
..        width: 70% !important;
..      }
..      .sd-col-4 {
..        width: 30% !important;
..      }
..    </style>

.. raw:: html

   <style>
     h1, h2, h3, h4, h5, h6 {
       text-align: center !important;
       font-weight: 500;
       font-size: 3rem !important;
       border-bottom: none;
     }
     a.headerlink {
       display: none;
       visibility: false;
     }
   </style>

.. raw:: html

   <style>
      p.rubric {
        font-weight: bold;
        font-size: 1.5rem;
        border-bottom: 0px solid var(--pst-color-accent);
      }
      p {
        font-family: 'ClearSans', var(--pst-font-family-base);
      }

   </style>

.. raw:: html

   <style>
      .bd-footer {
         border: none;
      }
   </style>

.. only:: html

   .. include:: _static/backgrounds/wormhole.rst

.. only:: html

   .. raw:: html

      <div style="display: none; visibility: hidden;">

   ####
   Home
   ####

   .. raw:: html
   
      </div>

.. only:: html

   .. grid:: 2
      :gutter: 0 0 0 0
      :class-container: sd-text-left

      .. grid-item-card::
         :columns: 12
         :padding: 0 0 0 0
         :text-align: center
         :class-card: sd-bg-transparent
         :shadow: none

         ^^^

         +++

         .. image:: /art/output/logo-text-bold-dark.svg
            :width: 500px
            :alt: Qhronology logo
            :align: center
            :class: only-dark

         .. image:: /art/output/logo-text-bold-light.svg
            :width: 500px
            :alt: Qhronology logo
            :align: center
            :class: only-light

      .. .. grid-item-card::
      ..    :columns: 4
      ..    :padding: 0 0 0 0
      ..    :text-align: left
      ..    :class-card: sd-bg-transparent
      ..    :shadow: none

      ..    ^^^

      ..    +++

      ..    .. image:: /art/output/clock-50fps-4sec-animated-90compressed.webp
      ..       :width: 120px
      ..       :alt: Clock
      ..       :align: left
      ..       :class: dark-light clock-animated


   ----

   .. rst-class:: centered
      
      **A Python package for resolving quantum time-travel paradoxes and**

      **performing general quantum information processing & computation**

   ----
   
   .. rst-class:: centered
      
      **Latest Version:** 1.0.0 | **Date:** June 2025
   
   ----

   .. https://sphinx-design.readthedocs.io/en/latest/grids.html

   .. grid:: 2
      :gutter: 2 3 4 4
      :padding: 2 2 2 2
      :class-container: sd-text-center

      .. grid-item-card:: Overview
         :columns: 6
         :text-align: center
         :class-card: sd-bg-muted
         :shadow: none

         .. raw:: html

            <svg xmlns="http://www.w3.org/2000/svg" width="72px" height="72px" viewBox="0 0 24 24"><title>information-outline</title><path fill="var(--pst-color-text-base)" d="M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z" /></svg>

         ^^^

         A brief overview of the features and functionality of Qhronology.

         +++

         .. button-ref:: part:overview
            :ref-type: ref
            :color: primary
            :click-parent:
            :expand:

            To the overview

      .. grid-item-card:: Theory
         :columns: 6
         :text-align: center
         :class-card: sd-bg-muted
         :shadow: none

         .. raw:: html

            <svg xmlns="http://www.w3.org/2000/svg" width="72px" height="72px" viewBox="0 0 24 24"><title>atom</title><path fill="var(--pst-color-text-base)" d="M12,11A1,1 0 0,1 13,12A1,1 0 0,1 12,13A1,1 0 0,1 11,12A1,1 0 0,1 12,11M4.22,4.22C5.65,2.79 8.75,3.43 12,5.56C15.25,3.43 18.35,2.79 19.78,4.22C21.21,5.65 20.57,8.75 18.44,12C20.57,15.25 21.21,18.35 19.78,19.78C18.35,21.21 15.25,20.57 12,18.44C8.75,20.57 5.65,21.21 4.22,19.78C2.79,18.35 3.43,15.25 5.56,12C3.43,8.75 2.79,5.65 4.22,4.22M15.54,8.46C16.15,9.08 16.71,9.71 17.23,10.34C18.61,8.21 19.11,6.38 18.36,5.64C17.62,4.89 15.79,5.39 13.66,6.77C14.29,7.29 14.92,7.85 15.54,8.46M8.46,15.54C7.85,14.92 7.29,14.29 6.77,13.66C5.39,15.79 4.89,17.62 5.64,18.36C6.38,19.11 8.21,18.61 10.34,17.23C9.71,16.71 9.08,16.15 8.46,15.54M5.64,5.64C4.89,6.38 5.39,8.21 6.77,10.34C7.29,9.71 7.85,9.08 8.46,8.46C9.08,7.85 9.71,7.29 10.34,6.77C8.21,5.39 6.38,4.89 5.64,5.64M9.88,14.12C10.58,14.82 11.3,15.46 12,16.03C12.7,15.46 13.42,14.82 14.12,14.12C14.82,13.42 15.46,12.7 16.03,12C15.46,11.3 14.82,10.58 14.12,9.88C13.42,9.18 12.7,8.54 12,7.97C11.3,8.54 10.58,9.18 9.88,9.88C9.18,10.58 8.54,11.3 7.97,12C8.54,12.7 9.18,13.42 9.88,14.12M18.36,18.36C19.11,17.62 18.61,15.79 17.23,13.66C16.71,14.29 16.15,14.92 15.54,15.54C14.92,16.15 14.29,16.71 13.66,17.23C15.79,18.61 17.62,19.11 18.36,18.36Z" /></svg>

         ^^^

         A collection of pedagogical articles discussing the mathematics behind quantum mechanics, including both its mathematical foundations and its applications to theories of antichronological time travel.

         +++

         .. button-ref:: part:theory
            :ref-type: ref
            :color: primary
            :click-parent:
            :expand:

            To the theory

      .. grid-item-card:: Documentation
         :columns: 6
         :text-align: center
         :class-card: sd-bg-muted
         :shadow: none

         .. raw:: html

            <svg xmlns="http://www.w3.org/2000/svg" width="72px" height="72px" viewBox="0 0 24 24"><title>book-open-variant-outline</title><path fill="var(--pst-color-text-base)" d="M12 21.5C10.65 20.65 8.2 20 6.5 20C4.85 20 3.15 20.3 1.75 21.05C1.65 21.1 1.6 21.1 1.5 21.1C1.25 21.1 1 20.85 1 20.6V6C1.6 5.55 2.25 5.25 3 5C4.11 4.65 5.33 4.5 6.5 4.5C8.45 4.5 10.55 4.9 12 6C13.45 4.9 15.55 4.5 17.5 4.5C18.67 4.5 19.89 4.65 21 5C21.75 5.25 22.4 5.55 23 6V20.6C23 20.85 22.75 21.1 22.5 21.1C22.4 21.1 22.35 21.1 22.25 21.05C20.85 20.3 19.15 20 17.5 20C15.8 20 13.35 20.65 12 21.5M11 7.5C9.64 6.9 7.84 6.5 6.5 6.5C5.3 6.5 4.1 6.65 3 7V18.5C4.1 18.15 5.3 18 6.5 18C7.84 18 9.64 18.4 11 19V7.5M13 19C14.36 18.4 16.16 18 17.5 18C18.7 18 19.9 18.15 21 18.5V7C19.9 6.65 18.7 6.5 17.5 6.5C16.16 6.5 14.36 6.9 13 7.5V19M14 16.35C14.96 16 16.12 15.83 17.5 15.83C18.54 15.83 19.38 15.91 20 16.07V14.57C19.13 14.41 18.29 14.33 17.5 14.33C16.16 14.33 15 14.5 14 14.76V16.35M14 13.69C14.96 13.34 16.12 13.16 17.5 13.16C18.54 13.16 19.38 13.24 20 13.4V11.9C19.13 11.74 18.29 11.67 17.5 11.67C16.22 11.67 15.05 11.82 14 12.12V13.69M14 11C14.96 10.67 16.12 10.5 17.5 10.5C18.41 10.5 19.26 10.59 20 10.78V9.23C19.13 9.08 18.29 9 17.5 9C16.18 9 15 9.15 14 9.46V11Z" /></svg>

         ^^^

         Detailed documentation of the Qhronology package including its various submodules and their respective functions, classes, and methods.

         +++

         .. button-ref:: part:documentation
            :ref-type: ref
            :color: primary
            :click-parent:
            :expand:

            To the documentation

      .. grid-item-card:: Examples
         :columns: 6
         :text-align: center
         :class-card: sd-bg-muted
         :shadow: none

         .. raw:: html

            <svg xmlns="http://www.w3.org/2000/svg" width="72px" height="72px" viewBox="0 0 24 24"><title>flask-outline</title><path fill="var(--pst-color-text-base)" d="M5,19A1,1 0 0,0 6,20H18A1,1 0 0,0 19,19C19,18.79 18.93,18.59 18.82,18.43L13,8.35V4H11V8.35L5.18,18.43C5.07,18.59 5,18.79 5,19M6,22A3,3 0 0,1 3,19C3,18.4 3.18,17.84 3.5,17.37L9,7.81V6A1,1 0 0,1 8,5V4A2,2 0 0,1 10,2H14A2,2 0 0,1 16,4V5A1,1 0 0,1 15,6V7.81L20.5,17.37C20.82,17.84 21,18.4 21,19A3,3 0 0,1 18,22H6M13,16L14.34,14.66L16.27,18H7.73L10.39,13.39L13,16M12.5,12A0.5,0.5 0 0,1 13,12.5A0.5,0.5 0 0,1 12.5,13A0.5,0.5 0 0,1 12,12.5A0.5,0.5 0 0,1 12.5,12Z" /></svg>

         ^^^

         A gallery of examples detailing the usage of Qhronology and its capabilities. Includes implementations of standard quantum algorithms and protocols, in addition to a selection of time-travel paradoxes.

         +++

         .. button-ref:: part:examples
            :ref-type: ref
            :color: primary
            :click-parent:
            :expand:

            To the examples

|

********
Features
********

.. only:: html

   .. grid:: 2
      :class-container: sd-text-left full-width

      .. grid-item-card::
         :columns: 7
         :padding: 0 0 0 0
         :text-align: left
         :class-card: sd-bg-black
         :shadow: none

         .. rubric:: Quantum computing simulations

         Designed to provide a powerful set of features with a simple and intuitive syntax, Qhronology facilitates the simulation of quantum computation, information processing, and algebraic calculations.

      .. grid-item-card::
         :columns: 5
         :padding: 0 0 0 0
         :text-align: center
         :class-card: sd-bg-white
         :shadow: none

         ^^^

         .. image:: /figures/output/circuit_algorithm_teleportation-light.png
            :scale: 40 %
            :alt: full adder quantum circuit
            :align: center
            :class: only-light

         .. image:: /figures/output/circuit_algorithm_teleportation-dark.png
            :scale: 40 %
            :alt: full adder quantum circuit
            :align: center
            :class: only-dark

         +++

      .. grid-item-card::
         :columns: 7
         :padding: 0 0 0 0
         :text-align: left
         :class-card: sd-bg-black
         :shadow: none

         .. rubric:: Quantum resolutions to antichronological time-travel paradoxes

         The fundamental indeterminism of quantum mechanics can be leveraged to provide resolutions to quantum formulations of classic time-travel paradoxes (such as the infamous *grandfather paradox*). A select few prescriptions by which this may be achieved, including Deutsch's model (D-CTCs) and the postselected teleportation prescription (P-CTCs), are implemented both as bare functions and wrapped class methods.

      .. grid-item-card::
         :columns: 5
         :padding: 0 0 0 0
         :text-align: center
         :class-card: sd-bg-white
         :shadow: none

         ^^^

         .. image:: /figures/output/circuit_ctc-light.png
            :scale: 40 %
            :alt: full adder quantum circuit
            :align: center
            :class: only-light

         .. image:: /figures/output/circuit_ctc-dark.png
            :scale: 40 %
            :alt: full adder quantum circuit
            :align: center
            :class: only-dark
         
         +++

      .. grid-item-card::
         :columns: 7
         :padding: 0 0 0 0
         :text-align: left
         :class-card: sd-bg-black
         :shadow: none

         .. rubric:: Quantum circuit visualization

         Quantum circuit diagrams provide a powerful picturalism through which any quantum process can be visualized as a network of quantum logic gates connected by wires. Qhronology provides this functionality for any quantum process constructed using its built-in classes.

         .. Alternative methods of visualization, such as that provided by the LaTeX *Quantikz* package, are under consideration for future development.

      .. grid-item-card::
         :columns: 5
         :padding: 0 0 0 0
         :text-align: center
         :class-card: sd-bg-white
         :shadow: none

         ^^^

         .. .. literalinclude:: /figures/text/text_examples_algorithms_generation_w.txt
         ..    :class: semigraphical

         .. only:: html

            .. image:: /figures/output/text_examples_algorithms_generation_w-dark.png
               :scale: 40 %
               :align: center
               :class: only-dark

            .. image:: /figures/output/text_examples_algorithms_generation_w-light.png
               :scale: 40 %
               :align: center
               :class: only-light

         .. only:: latex

            .. raw:: latex

               \vspace{1em}

            .. image:: /figures/output/text_examples_algorithms_generation_w-light.png
               :scale: 40 %
               :align: center
               :class: light-dark hidden


         +++

      .. grid-item-card::
         :columns: 7
         :padding: 0 0 0 0
         :text-align: left
         :class-card: sd-bg-black
         :shadow: none

         .. rubric:: Numerous examples

         Bundled with the project is a small collection of complete examples that showcase its capabilities and syntax. These are divided into two categories: *quantum algorithms and protocols* and *quantum closed timelike curves*. The former contains implementations of canonical algorithms in quantum computing, while the latter consists of more exotic circuits that use quantum mechanics to resolve paradoxical scenarios of antichronological time travel.

      .. grid-item-card::
         :columns: 5
         :padding: 0 0 0 0
         :text-align: center
         :class-card: sd-bg-white
         :shadow: none

         ^^^

         .. image:: /figures/output/circuit_algorithm_adder_full-light.png
            :scale: 40 %
            :alt: full adder quantum circuit
            :align: center
            :class: only-light

         .. image:: /figures/output/circuit_algorithm_adder_full-dark.png
            :scale: 40 %
            :alt: full adder quantum circuit
            :align: center
            :class: only-dark
         
         +++

      .. grid-item-card::
         :columns: 7
         :padding: 0 0 0 0
         :text-align: left
         :class-card: sd-bg-black
         :shadow: none

         .. rubric:: Extensive documentation

         All of the functions, classes, and methods in each of the various submodules have been rigorously detailed in their respective sections within the documentation. This includes multiple examples of usage for each, aiding the user's understanding of every available feature.


      .. grid-item-card::
         :columns: 5
         :padding: 0 0 0 0
         :text-align: center
         :class-card: sd-bg-white
         :shadow: none

         ^^^

         .. image:: /figures/output/diagram_bloch_sphere-light.png
            :scale: 40 %
            :alt: full adder quantum circuit
            :align: center
            :class: only-light

         .. image:: /figures/output/diagram_bloch_sphere-dark.png
            :scale: 40 %
            :alt: full adder quantum circuit
            :align: center
            :class: only-dark
         
         +++

      .. grid-item-card::
         :columns: 7
         :padding: 0 0 0 0
         :text-align: left
         :class-card: sd-bg-black
         :shadow: none

         .. rubric:: Foundational theory

         All of the underlying mathematics upon which Qhronology is built is presented as a series of pedagogical reference articles within the documentation. This includes sections on the mathematical foundations of quantum mechanics (Hilbert spaces, linear operators, composite systems, etc.), quantum theory on both discrete and continuous Hilbert spaces, a brief overview of the quantum circuitry picturalism, and physical theories of time travel (both classical and quantum).

         The aim of this theory is to serve as a comprehensive and complete reference for basic quantum mechanics and the physical theories of time travel, thereby enabling the keen user to embark upon further research into these fascinating areas of study.

      .. grid-item-card::
         :columns: 5
         :padding: 0 0 0 0
         :text-align: center
         :class-card: sd-bg-white
         :shadow: none

         ^^^

         .. image:: /figures/output/diagram_spacetime_minkowski-light.png
            :width: 450px
            :alt: full adder quantum circuit
            :align: center
            :class: only-light

         .. image:: /figures/output/diagram_spacetime_minkowski-dark.png
            :width: 450px
            :alt: full adder quantum circuit
            :align: center
            :class: only-dark
         
         +++

   |

      Can't find what you're looking for? Try using the :ref:`search`.

.. .. toctree::
..    :caption: Contents:
..    :maxdepth: 2

..    structure

.. .. toctree::
..    :hidden:
..    :maxdepth: 2

..    documentation/text/part

.. .. toctree::
..    :hidden:
..    :maxdepth: 2

..    documentation/text/examples/part

.. .. toctree::
..    :caption: Theory
..    :maxdepth: 2

..    documentation/text/theory/part

.. toctree::
   :maxdepth: 3
   :hidden:

   ../../README.rst
   /text/theory/part-theory
   /text/documentation/part-documentation
   /text/examples/part-examples
   /text/live/part-live
   /text/appendix/part-appendix

.. .. only:: html

..    .. bibliography::
..       :filter: docname in docnames

.. .. only:: latex

..   .. bibliography::