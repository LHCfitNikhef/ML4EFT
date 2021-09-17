Symbol Vf, Af,Mz,s,t,u,Mh,SW2;
Vector p1,p2,p3,p4;
Indices mu,al,rho,nu;

Local F = (1/4)*g_(1,p2,mu)*(Vf-Af*g5_(1))*g_(1,p1)*(Vf+Af*g5_(1))*g_(1,al)*(
	+(-d_(mu,al)+p4(mu)*p4(al)/Mz^2)
	+(p1(mu)+p2(mu))*(p1(rho)+p2(rho))*(p1(al)+p2(al))*(p1(nu)+p2(nu))*(-d_(rho,nu)+p4(rho)*p4(nu)/Mz^2)/Mz^4
	+(p1(mu)+p2(mu))*(p1(rho)+p2(rho))*(d_(rho,al)-p4(rho)*p4(al)/Mz^2)/Mz^2
	+(p1(al)+p2(al))*(p1(nu)+p2(nu))*(d_(mu,nu)-p4(mu)*p4(nu)/Mz^2)/Mz^2
	);

trace4,1;
*Print +s;
.sort

id p1.p2 = s/2;
id p1.p1 = 0;
id p2.p2 = 0;
id p1.p4 = (Mz^2-t)/2;
id p4.p4 = Mz^2;
id p2.p4 = (Mz^2-u)/2;
*Print +s;
.sort

*id Af = 1/2;
*id Vf = 1/2-4/3*SW2;

*id u = Mz^2+Mh^2-s-t;
Print +s;
.end
