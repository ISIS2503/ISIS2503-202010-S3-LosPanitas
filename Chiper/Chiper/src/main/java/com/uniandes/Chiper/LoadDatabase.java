package com.uniandes.Chiper;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
class LoadDatabase {

  private static final Logger log = LoggerFactory.getLogger(LoadDatabase.class);

  @Bean
  CommandLineRunner initDatabase(PedidoRepository repository) {

    return args -> {
      log.info("Preloading " + repository.save(new Pedido("Coca-Cola", "Unidades:1000")));
      log.info("Preloading " + repository.save(new Pedido("Papas Margarita", "Unidades:1000")));
    };
  }
}
