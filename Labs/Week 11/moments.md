# Moments of Inertia
$$\bar{x} = \dfrac{M_y}{m} $$
$$\bar{y} = \dfrac{M_x}{m} $$
$$\rho(x,y) = \lim_{\Delta A \rightarrow 0} \dfrac{\Delta m}{\Delta A $$
$$m = \iint_R \, dm = \iint_R \rho (x,y) dA = \int_{x=0}^{x=3} \int_{y=0}^{y=3-x} xy \, dy \, dx = \int_{x=0}^{x=3} \left[ \left. x \dfrac{y^2}{2} \right|_{y=0}^{y=3} \right] \, dx = \int_{x=0}^{x=3} \dfrac{1}{2} x (3 - x)^2 dx = \left.\left[ \dfrac{9x^2}{4} - x^3 + \dfrac{x^4}{8} \right]\right|_{x=0}^{x=3} = \dfrac{27}{8} $$
$$M_x = \lim_{k,l \rightarrow \infty} \sum_{i=1}^k \sum_{j=1}^l (y_{ij}^*)m_{ij} = \lim_{k,l \rightarrow \infty} \sum_{i=1}^k \sum_{j=1}^l (y_{ij}^*) \rho(x_{ij}^*,y_{ij}^*) \,\Delta A = \iint_R y\rho (x,y) \,d $$
$$M_y = \lim_{k,l \rightarrow \infty} \sum_{i=1}^k \sum_{j=1}^l (x_{ij}^*)m_{ij} = \lim_{k,l \rightarrow \infty} \sum_{i=1}^k \sum_{j=1}^l (x_{ij}^*) \rho(x_{ij}^*,y_{ij}^*) \,\Delta A = \iint_R x\rho (x,y) \,d $$
$$M_x = \iint_R y\rho (x,y) \,dA = \int_{x=0}^{x=3} \int_{y=0}^{y=3-x} x y^2 \, dy \, dx = \dfrac{81}{20} $$
$$M_y = \iint_R x\rho (x,y) \,dA = \int_{x=0}^{x=3} \int_{y=0}^{y=3-x} x^2 y \, dy \, dx = \dfrac{81}{20} $$
$$\bar{x} = \dfrac{M_y}{m} = \dfrac{\iint_R x\rho (x,y) \,dA}{\iint_R \rho (x,y)\,dA} $$
$$\bar{y} = \dfrac{M_x}{m} = \dfrac{\iint_R y\rho (x,y) \,dA}{\iint_R \rho (x,y)\,dA $$
$$\bar{x} = \dfrac{M_y}{m} = \dfrac{\iint_R x\rho (x,y) \,dA}{\iint_R \rho (x,y)\,dA} = \dfrac{81/20}{27/8} = \dfrac{6}{5} $$
$$\bar{y} = \dfrac{M_x}{m} = \dfrac{\iint_R y\rho (x,y) \,dA}{\iint_R \rho (x,y)\,dA} = \dfrac{81/20}{27/8} = \dfrac{6}{5} $$
$$x_c = \dfrac{M_y}{m} = \dfrac{\iint_R x \, dA}{\iint_R \,dA} = \dfrac{9/2}{9/2} = 1 $$
$$y_c = \dfrac{M_x}{m} = \dfrac{\iint_R y \, dA}{\iint_R \,dA} = \dfrac{9/2}{9/2} = 1 $$
$$x_c = \dfrac{M_y}{m} = \dfrac{\iint_R x \, dA}{\iint_R \,dA} \, \text{and} \, y_c = \dfrac{M_x}{m} = \dfrac{\iint_R y \, dA}{\iint_R \,dA} $$
$$m = \iint_R \,dm = \iint_R \rho (x,y) \,dA = \int_{x=0}{x=2} \int_{y=0}^{y=x^2} (x + y) dy \, dx = \int_{x=0}^{x=2} \left[\left. xy + \dfrac{y^2}{2}\right|_{y=0}^{y=x^2} \right] \,d $$
$$= \int_{x=0}^{x=2} \left[ x^3 + \dfrac{x^4}{2} \right] dx = \left.\left[ \dfrac{x^4}{4} + \dfrac{x^5}{10}\right] \right|_{x=0}^{x=2} = \dfrac{36}{5} $$
$$M_x = \iint_R y \rho (x,y) \,dA = \int_{x=0}^{x=2} \int_{y=0}^{y=x^2} y(x + y) \,dy \, dx = \dfrac{80}{7} $$
$$M_y = \iint_R x \rho (x,y) \,dA = \int_{x=0}^{x=2} \int_{y=0}^{y=x^2} x(x + y) \,dy \, dx = \dfrac{176}{15} $$
$$\bar{x} = \dfrac{M_y}{m} = \dfrac{\iint_R x \rho (x,y) \,dA}{\iint_R \rho (x,y)\,dA} = \dfrac{176/15}{36/5} = \dfrac{44}{27} $$
$$\bar{y} = \dfrac{M_x}{m} = \dfrac{\iint_R y \rho (x,y) \,dA}{\iint_R \rho (x,y)\,dA} = \dfrac{80/7}{36/5} = \dfrac{100}{63} $$
$$x_c = \dfrac{M_y}{m} = \dfrac{\iint_R x \, dA}{\iint_R dA} \, and \, y_c = \dfrac{M_x}{m} = \dfrac{\iint_R y \, dA}{\iint_R dA} $$
$$x_c = \dfrac{M_y}{m} = \dfrac{\iint_R x \, dA}{\iint_R dA} = \dfrac{\int_{x=1}^{x=3} \int_{y=0}^{y=e^x} x \, dy \, dx}{\int_{x=1}^{x=3} \int_{y=0}^{y=e^x} \,dy \, dx} = \dfrac{\int_{x=1}^{x=3} xe^x dx}{\int_{x=1}^{x=3} e^x dx} = \dfrac{2e^3}{e^3 - e} = \dfrac{2e^2}{e^2 - 1} $$
$$y_c = \dfrac{M_x}{m} = \dfrac{\iint_R y \, dA}{\iint_R dA} = \dfrac{\int_{x=1}^{x=3} \int_{y=0}^{y=e^x} y \, dy \, dx}{\int_{x=1}^{x=3} \int_{y=0}^{y=e^x} \,dy \, dx} = \dfrac{\int_{x=1}^{x=3} \dfrac{e^{2x}}{2} dx}{\int_{x=1}^{x=3} e^x dx} =\dfrac{\dfrac{1}{4} e^2 (e^4 - 1)}{e(e^2 - 1)} = \dfrac{1}{4} e(e^2 + 1) $$
$$(x_c,y_c) = \left( \dfrac{2e^2}{e^2 - 1}, \dfrac{1}{4} e(e^2 + 1)\right) $$
$$I_x = \lim_{k,l\rightarrow \infty} \sum_{i=1}^k \sum_{j=1}^l (y_{ij}^*)^2 m_{ij} = \lim_{k,l\rightarrow \infty} \sum_{i=1}^k \sum_{j=1}^l (y_{ij}^*)^2 \rho (x_{ij}^*, y_{ij}^*) \,\Delta A = \iint_R y^2 \rho(x,y)\,dA $$
$$I_y = \lim_{k,l\rightarrow \infty} \sum_{i=1}^k \sum_{j=1}^l (x_{ij}^*)^2 m_{ij} = \lim_{k,l\rightarrow \infty} \sum_{i=1}^k \sum_{j=1}^l (x_{ij}^*)^2 \rho (x_{ij}^*, y_{ij}^*) \,\Delta A = \iint_R x^2 \rho(x,y)\,dA $$
$$I_0 = I_x + I_y = \iint_R (x^2 + y^2) \rho (x,y) \,dA $$
$$I_x = \iint_R y^2 \rho(x,y) \,dA = \int_{x=0}^{x=2} \int_{y=0}^{y=x} xy^3 \,dy \, dx = \dfrac{8}{3} $$
$$I_y = \iint_R x^2 \rho(x,y) \,dA = \int_{x=0}^{x=2} \int_{y=0}^{y=x} x^3y \,dy \, dx = \dfrac{16}{3} $$
$$I_0 = \iint_R (x^2 + y^2) \rho(x,y) \,dA = \int_0^2 \int_0^x (x^2 + y^2) xy \, dy \, dx = I_x + I_y =  $$
$$I_x = \int_{x=0}^{x=2} \int_{y=0}^{y=x} y^2 \sqrt{xy} \, dy \, dx = \dfrac{64}{35 $$
$$I_y = \int_{x=0}^{x=2} \int_{y=0}^{y=x} x^2 \sqrt{xy} \, dy \, dx = \dfrac{64}{35} $$
$$I_0 = \int_{x=0}^{x=2} \int_{y=0}^{y=x} (x^2 + y^2) \sqrt{xy} \, dy \, dx = \dfrac{128}{21 $$
$$R_x = \sqrt{\dfrac{I_x}{m}}, \, R_y = \sqrt{\dfrac{I_y}{m}}, \, and \, R_0 = \sqrt{\dfrac{I_0}{m}} $$
$$\begin{align} R_x = \sqrt{\dfrac{I_x}{m}} = \sqrt{\dfrac{8/3}{2}} = \sqrt{\dfrac{8}{6}} = \dfrac{2\sqrt{3}}{3},\\R_y = \sqrt{\dfrac{I_y}{m}} = \sqrt{\dfrac{16/3}{2}} = \sqrt{\dfrac{8}{3}} = \dfrac{2\sqrt{6}}{3}, \\R_0 = \sqrt{\dfrac{I_0}{m}} = \sqrt{\dfrac{8}{2}} = \sqrt{4} = 2.\end{align $$
$$m = \iiint_Q \rho(x,y,z) \,dV $$
$$M_{xy} = \iiint_Q z\rho (x,y,z) \,dV, \, M_{xz} = \iiint_Q y\rho(x,y,z) \,dV, \, M_{yz} = \iiint_Q x\rho(x,y,z) \,dV $$
$$\bar{x} = \dfrac{M_{yz}}{m}, \, \bar{y} = \dfrac{M_{xz}}{m}, \, \bar{z} = \dfrac{M_{xy}}{m} $$
$$I_x = \iiint_Q (y^2 + z^2) \, \rho (x,y,z) \, dV $$
$$I_y = \iiint_Q (x^2 + z^2) \, \rho (x,y,z) \, dV $$
$$I_z = \iiint_Q (x^2 + y^2) \, \rho (x,y,z) \, dV $$
$$m = \iiint_Q \rho (x,y,z) \,dV = \int_{x=0}^{x=6} \int_{y=0}^{y=1/2(6-x)} \int_{z=0}^{z=1/3(6-x-2y)} x^2 yz \, dz \, dy \, dx = \dfrac{108}{35 $$
$$M_{xy} = \iiint_Q z\rho (x,y,z) \,dV = \int_{x=0}^{x=6} \int_{y=0}^{y=\frac{1}{2}(6-x)} \int_{z=0}^{z=\frac{1}{3}(6-x-2y)} x^2 yz^2 \,dz \, dy \, dx = \dfrac{54}{35} \approx 1.543 $$
$$M_{xz} = \iiint_Q y\rho (x,y,z) \,dV = \int_{x=0}^{x=6} \int_{y=0}^{y=\frac{1}{2}(6-x)} \int_{z=0}^{z=\frac{1}{3}(6-x-2y)} x^2 y^2z \, dz \, dy \, dx = \dfrac{81}{35} \approx 2.314 $$
$$M_{yz} = \iiint_Q x\rho (x,y,z) \,dV = \int_{x=0}^{x=6} \int_{y=0}^{y=\frac{1}{2}(6-x)} \int_{z=0}^{z=\frac{1}{3}(6-x-2y)} x^3 yz \, dz \, dy \, dx = \dfrac{243}{35} \approx 6.943 $$
$$\bar{x} = \dfrac{M_{yz}}{m}, \, \bar{y} = \dfrac{M_{xz}}{m}, \, \bar{z} = \dfrac{M_{xy}}{m} $$
$$\bar{x} = \dfrac{M_{yz}}{m} = \dfrac{243/35}{108/35} = \dfrac{243}{108} = 2.25 $$
$$\bar{y} = \dfrac{M_{xz}}{m} = \dfrac{81/35}{108/35} = \dfrac{81}{108} = 0.75 $$
$$\bar{z} = \dfrac{M_{xy}}{m} = \dfrac{54/35}{108/35} = \dfrac{54}{108} = 0. $$
$$I_x = \iiint_Q (y^2 + z^2) \rho(x,y,z) \,dV $$
$$I_y = \iiint_Q (x^2 + z^2) \rho(x,y,z) \,dV $$
$$I_z = \iiint_Q (x^2 + y^2) \rho(x,y,z) \,dV \, with \, \rho(x,y,z) = x^2yz $$
$$\begin{align*} I_x = \iiint_Q (y^2 + z^2) x^2 \rho(x,y,z) \,dV \$$
$$4pt] = \int_{x=0}^{x=6} \int_{y=0}^{y=\frac{1}{2}(6-x)} \int_{z=0}^{z=\frac{1}{3}(6-x-2y)} (y^2 + z^2) x^2 yz \, dz \, dy \, dx = \dfrac{117}{35} \approx 3.343,\end{align*}$$
$$\begin{align*} I_y = \iiint_Q (x^2 + z^2) x^2 \rho(x,y,z) \,dV \$$
$$4pt] = \int_{x=0}^{x=6} \int_{y=0}^{y=\frac{1}{2}(6-x)} \int_{z=0}^{z=\frac{1}{3}(6-x-2y)} (x^2 + z^2) x^2 yz \, dz \, dy \, dx = \dfrac{684}{35} \approx 19.543, \end{align*}$$
$$\begin{align*} I_z = \iiint_Q (x^2 + y^2) x^2 \rho(x,y,z) \,dV \$$
$$4pt] = \int_{x=0}^{x=6} \int_{y=0}^{y=\frac{1}{2}(6-x)} \int_{z=0}^{z=\frac{1}{3}(6-x-2y)} (x^2 + y^2) x^2 yz \, dz \, dy \, dx = \dfrac{729}{35} \approx 20.829. \end{align*}$$
$$m = \iint_R \rho (x,y) \,dA $$
$$M_x = \iint_R y\rho(x,y) \,dA \, and \, M_y = \iint_R x\rho(x,y) \,dA $$
$$I_x = \iint_R y^2 \rho(x,y) \,dA, \, I_y = \iint_R x^2 \rho(x,y) \,dA, \, and \, I_0 = I_x + I_y = \iint_R (x^2 + y^2) \rho(x,y) \,dA $$
$$m = \iiint_Q \rho (x,y,z) \,dV $$
$$M_{xy} = \iiint_Q z\rho (x,y,z)\,dV, \, M_{xz} = \iiint_Q y\rho (x,y,z)\,dV, \, M_{yz} = \iiint_Q x\rho (x,y,z)\,d $$
$$I_x = \iiint_Q (y^2 + z^2) \, \rho (x,y,z) \, dV, \, I_y = \iiint_Q (x^2 + z^2) \, \rho (x,y,z) \, dV, \, I_z = \iiint_Q (x^2 + y^2) \, \rho (x,y,z) \, dV $$
$$m = \lim_{k,l \rightarrow\infty} \sum_{i=1}^k \sum_{j=1}^l m_{ij} = \lim_{k,l \rightarrow\infty} \sum_{i=1}^k \sum_{j=1}^l \rho (x_{ij}^*, y_{ij}^*) \,\Delta A = \iint_R \rho(x,y) \,d $$
$$M_x = \lim_{k,l \rightarrow\infty} \sum_{i=1}^k \sum_{j=1}^l (y_{ij}^*) m_{ij} = \lim_{k,l \rightarrow\infty} \sum_{i=1}^k \sum_{j=1}^l (y_{ij}^*) \rho (x_{ij}^*, y_{ij}^*) \,\Delta A = \iint_R y\rho(x,y)\,d $$
$$M_y = \lim_{k,l \rightarrow\infty} \sum_{i=1}^k \sum_{j=1}^l (x_{ij}^*) m_{ij} = \lim_{k,l \rightarrow\infty} \sum_{i=1}^k \sum_{j=1}^l (x_{ij}^*) \rho (x_{ij}^*, y_{ij}^*) \,\Delta A = \iint_R x\rho(x,y)\,d $$
$$\bar{x} = \dfrac{M_y}{m} = \dfrac{\iint_R x\rho (x,y) \,dA}{\iint_R \rho (x,y) \,dA} \, and \, \bar{y} = \dfrac{M_x}{m} = \dfrac{\iint_R y\rho (x,y) \,dA}{\iint_R \rho (x,y) \,dA $$
