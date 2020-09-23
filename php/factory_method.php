<?php

abstract class Product {
	abstract public function show(): string;
}

class ProductOne extends Product {
	public function show(): string {
		return "product one";
	}
}

class ProductTwo extends Product {
	public function show(): string {
		return "product two";
	}
}

abstract class Creator {
	abstract public function factoryMethod(): Product;

	public function showOutput(): void {
		$product = $this->factoryMethod();

		echo "output: {$product->show()}";
	}
}

class ConcreteCreatorProductOne extends Creator {
	public function factoryMethod(): Product {
		return new ProductOne();
	}
}

class ConcreteCreatorProductTwo extends Creator {
	public function factoryMethod(): Product {
		return new ProductTwo();
	}
}

function clientCode(Creator $creator): void {
	$creator->showOutput();
}

clientCode(new ConcreteCreatorProductTwo());
