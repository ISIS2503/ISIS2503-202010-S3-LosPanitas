package com.uniandes.Chiper;

class PedidoNotFoundException extends RuntimeException {

	  PedidoNotFoundException(Long id) {
	    super("Could not find pedido " + id);
	  }
	}
