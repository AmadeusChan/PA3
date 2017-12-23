package decaf.tac;

import decaf.tac.Temp;

public class ComplexTemp extends Temp {
	public Temp re, im;

	public ComplexTemp() {
		re = Temp.createTempI4();
		im = Temp.createTempI4();
	}
}
