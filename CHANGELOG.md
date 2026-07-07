# Changelog

## [1.1.0](https://github.com/lgbishop/qhronology/tree/1.1.0) (2026-07-07)

[Full Changelog](https://github.com/lgbishop/qhronology/compare/1.0.3...1.1.0)

### Package:

- Update `print()` methods for `QuantumObject` and descendents. ([0f7fee3](https://github.com/lgbishop/qhronology/commit/0f7fee36c66c57ad40938ca04b7fcd41880a86ac))
- Add a `visible` argument to `QuantumCircuit.diagram()` method and update examples. ([bb1f667](https://github.com/lgbishop/qhronology/commit/bb1f667d32805fd3f9cabed1e290224321d35b2c))
- Change the default circuit input state from being the maximally mixed state to the zero state. ([b927820](https://github.com/lgbishop/qhronology/commit/b927820bc97800ee660eb504e8f1335e856d2832))
- Add a `maximum_entropy` argument to D-CTC prescription. ([0e4bf12](https://github.com/lgbishop/qhronology/commit/0e4bf122569115160751de4dfffdf9d1716c7efe))
- Allow keyword arguments passed to `QuantumCTC.__init__()` to override values contained within the `QuantumCircuit` instance given to the `circuit` argument. ([e1eae7a](https://github.com/lgbishop/qhronology/commit/e1eae7ab20f8530ca25834b9118cd15a763e7742))
- Add the ability to perform computations numerically. ([08a8466](https://github.com/lgbishop/qhronology/commit/08a846679cd7df43df9fa6f8941f5b80ca49c06f))
- Change `conditions` to `substitutions` to better convey its purpose. ([28e7d80](https://github.com/lgbishop/qhronology/commit/28e7d8050ea70a27f48f02f2d528e7caeac88cca))
- Allow gates in a circuit to automatically expand to more systems. ([49534c4](https://github.com/lgbishop/qhronology/commit/49534c49a9f85bff31b9a1288373cbc586a65149))
- Add a `Unitary` gate. ([901a7ab](https://github.com/lgbishop/qhronology/commit/901a7abe12c85b93ff06585e633051bd74bf7b9b))

### Documentation:

- Add example logs and associated testing scripts. ([30fdeca](https://github.com/lgbishop/qhronology/commit/30fdeca53c5f8f06ae3c49d4d8807c26962ed5d3))
- Add script for testing all code snippets in the `.rst` files. ([72f32ff](https://github.com/lgbishop/qhronology/commit/72f32ffe880eba3b728fe980acd72ad74cac6de7))

#### PDF:

- Add a script for making a printable version. ([6422359](https://github.com/lgbishop/qhronology/commit/64223593620396edc673ce768d7a7ff2b83b50fc))
- Fix alignment of chapter title underline. ([44f09c3](https://github.com/lgbishop/qhronology/commit/44f09c3c4beeb339d298c57762577ec32e362b2d))

#### Website:

- Add SciPy to the live environment. ([c0c3fc0](https://github.com/lgbishop/qhronology/commit/c0c3fc030c39981834cffb823ecacda4a6773bc2))
- Resize semigraphical diagrams. ([e1e6ae8](https://github.com/lgbishop/qhronology/commit/e1e6ae87d691ad2bedac3fccc587ae755f04b004))
- Improve flexing of cards on title page for small displays. ([36eaf94](https://github.com/lgbishop/qhronology/commit/36eaf942f817dc79ad6a48008b00b4deb3c924c9))

## [1.0.3](https://github.com/lgbishop/qhronology/tree/1.0.3) (2026-03-05)

[Full Changelog](https://github.com/lgbishop/qhronology/compare/1.0.2...1.0.3)

### Package:

- Optimize `is_vector` and `input_is_vector` properties. ([36bd114](https://github.com/lgbishop/qhronology/commit/36bd11408e413289c1d6effceb38f0ded8e8e5ab)) (Of its many effects, this makes circuit diagrams render significantly faster.)
- Add `merge` kwarg to `QuantumCTC.input()` method to fix override incompatibility with `QuantumCircuit.input()`. ([97cbff2](https://github.com/lgbishop/qhronology/commit/97cbff22bd2142099e75b6b5dac740f7a3deac53))
- Fix `__repr__`, `matrix` property, and `output()` method of `QuantumCTC` class. ([4e2616b](https://github.com/lgbishop/qhronology/commit/4e2616b6155e1725f8adf8c54a7ca857b23fed6a))
- Prepend an underscore to the `VisualizationMixin.diagram_column()` method. ([140e0e7](https://github.com/lgbishop/qhronology/commit/140e0e7f461f0d6c535f978457c2102685ed4567)) (To better reflect its intended internal-only status.)
- Add and incorporate custom `expr` type. ([42770b4](https://github.com/lgbishop/qhronology/commit/42770b41bac4495b80c142d017bb9596e494a136)) (To better distinguish between single-symbol characters and multiple-symbol expressions in type hints.)

### Documentation:

- Mention the project's ([technical paper](https://arxiv.org/abs/2601.17459)). ([4ebbb98](https://github.com/lgbishop/qhronology/commit/4ebbb989f0a75a255ec9656d471b571e712c8756))
- Add missing `QuantumCTC.matrix` property. ([016eed0](https://github.com/lgbishop/qhronology/commit/016eed08f4c2d4eff5c5533c1e807d689d52cc62))
- Format all docstrings to soft wrap. ([94f515b](https://github.com/lgbishop/qhronology/commit/94f515b833d96cc7661230da11d5c57772ad7877))
- Update durations of examples. ([2a4847e](https://github.com/lgbishop/qhronology/commit/2a4847e2fa73f7d85b45708343590fc0212d1e9b))
- Update contact email address in all project documentation. ([4802320](https://github.com/lgbishop/qhronology/commit/4802320d830b260d97290eacf1982a6cc1fe167a))
- Update website to new top-level domain (from `.com` to `.org`). ([ed5ca7e](https://github.com/lgbishop/qhronology/commit/ed5ca7e4258d61bd317b4130297eca22708713ae))

#### PDF:

- Visual overhaul of the code blocks. ([82d3da9](https://github.com/lgbishop/qhronology/commit/82d3da9f8230c4be3b09fca82fc15170b746870e))

#### Website:

- Update syntax highlighting for signatures of class properties. ([90f3695](https://github.com/lgbishop/qhronology/commit/90f3695e24ecbc7a8b82713f9070cc5df3cfd883))

## [1.0.2](https://github.com/lgbishop/qhronology/tree/1.0.2) (2026-01-24)

[Full Changelog](https://github.com/lgbishop/qhronology/compare/1.0.1...1.0.2)

### Package:

- Fix: Notation property for conjugation of vectors. ([579cba5](https://github.com/lgbishop/qhronology/commit/579cba54bfc122833ae227d89577eaa3c3c14dff))
- Fix: Ordering of boundaries list in `partition_systems`. ([2dfd3eb](https://github.com/lgbishop/qhronology/commit/2dfd3ebe757fe288ffc7f6a7256fbab0b2ff0d04))
- Fix: Measurement gate for multipartite operators. ([9ff3d7e](https://github.com/lgbishop/qhronology/commit/9ff3d7e2b3919d01e1c4b862f6bbe80708c4342c))
- Fix: Entropy and mutual information functions, reorder internal logic of all quantities. ([398a808](https://github.com/lgbishop/qhronology/commit/398a80860c26f5723f1846de90036be48c078ded))
- Add `merge` argument to `QuantumCircuit.input()` method and enhance its labelling functionality. ([6053055](https://github.com/lgbishop/qhronology/commit/605305515a3f9c3058948cbb0fe57d83df64ca90))
- Change state edge connectors from braces to parentheses in the diagram `'ascii'` style ([0544c3c](https://github.com/lgbishop/qhronology/commit/0544c3cb9e46a0453aaa2a4c44c902666436b7e7))

### Documentation:

- Add a generalized W state example. ([ee855c1](https://github.com/lgbishop/qhronology/commit/ee855c166e79911a15fd937e69b5d372c9616e50))
- Update bibliography and fix all citations. ([3ddcc35](https://github.com/lgbishop/qhronology/commit/3ddcc351e9d19b50b33d461cfc9d3fea2d70d3ae)) ([12dcd4e](https://github.com/lgbishop/qhronology/commit/12dcd4ed590876c0725d3e647ec2bf2ae463075e))

#### Website:

- Add Cousine as primary monospace font. ([964039d](https://github.com/lgbishop/qhronology/commit/964039da9668ad0c83d27237e4c33435ad57e0fb))

## [1.0.1](https://github.com/lgbishop/qhronology/tree/1.0.1) (2025-07-01)

[Full Changelog](https://github.com/lgbishop/qhronology/compare/1.0.0...1.0.1)

### Package:

- Introduce comprehensive simplification functionality. ([7570b1d](https://github.com/lgbishop/qhronology/commit/7570b1d57e24cfb395d543fe970f6050e06f74f3))
- Upgrade the `stringify` function and the associated `print` method. ([2780611](https://github.com/lgbishop/qhronology/commit/2780611481bfa5291c758f33d71ea608c6fbf201))

### Documentation:

- Add a generalized GHZ state example. ([b9c7feb](https://github.com/lgbishop/qhronology/commit/b9c7feb7529875a34214ef3956ffbaedb200b015))
- Expand the unproven-theorem paradox example. ([0fadbcd](https://github.com/lgbishop/qhronology/commit/0fadbcd359eb9522d38d4ea684b52520012705d0))

#### Website:

- Add live Qhronology testing environment. ([83e3a6f](https://github.com/lgbishop/qhronology/commit/83e3a6fd63ae826d22b485543830c3f85bb375fb))

## [1.0.0](https://github.com/lgbishop/qhronology/tree/1.0.0) (2025-06-08)

Initial release.
