<?php

interface Product {
    public function show(): string;
    public function color(): string;
}

class ProductGreenOne implements Product {
	public function show(): string {
		return "product green 1";
    }
    
    public function color(): string {
        return "i am green";
    }
}

class ProductBlueOne implements Product {
	public function show(): string {
		return "product blue 1";
    }
    
    public function color(): string {
        return "i am blue";
    }
}

class ProductGreenTwo implements Product {
	public function show(): string {
		return "product green 2";
    }
    
    public function color(): string {
        return "i am green";
    }
}

class ProductBlueTwo implements Product {
	public function show(): string {
		return "product blue 2";
    }
    
    public function color(): string {
        return "i am blue";
    }
}

interface Creator {
	public function createProductBlue(): Product;
	public function createProductGreen(): Product;
}

class ConcreteProductCreatorOne implements Creator {
	public function createProductGreen(): ProductGreenOne {
        return new ProductGreenOne();
    }

    public function createProductBlue(): ProductBlueOne {
        return new ProductBlueOne();
    }
}

class ConcreteProductCreatorTwo implements Creator {
	public function createProductGreen(): ProductGreenTwo {
        return new ProductGreenTwo();
    }

    public function createProductBlue(): ProductBlueTwo {
        return new ProductBlueTwo();
    }
}

interface CreatorColor {
    public function createProductOne(): Product;
    public function createProductTwo(): Product;
}

class ConcreteProductCreatorGreen implements CreatorColor {
    public function createProductOne(): ProductGreenOne {
        return new ProductGreenOne();
    }

    public function createProductTwo(): ProductGreenTwo {
        return new ProductGreenTwo();
    }
}

function client(Creator $creator): void {
    $product = $creator->createProductBlue();

    echo "{$product->show()} - {$product->color()}\n";
}

function clientColor(CreatorColor $creator): void {
    $product = $creator->createProductTwo();

    echo "{$product->show()} - {$product->color()}\n";
}

client(new ConcreteProductCreatorOne());

clientColor(new ConcreteProductCreatorGreen());
