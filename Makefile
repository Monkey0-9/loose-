# Loose AI - Polyglot Build System
# Handles compilation and verification of multi-language modules.

.PHONY: all clean test build-go build-rust build-cpp build-zig build-java

all: build-go build-rust build-cpp build-zig build-java

# 1. Go Health Auditor
build-go:
	@echo "Building Go Health Auditor..."
	@cd polyglot_core/go_health_checker && go build -o ../../bin/go-audit main.go

# 2. Rust Secure Compute
build-rust:
	@echo "Building Rust Secure Compute..."
	@cd polyglot_core/rust_secure_compute && cargo build --release
	@cp polyglot_core/rust_secure_compute/target/release/rust_secure_compute bin/rust-secure

# 3. C++ Math Engine
build-cpp:
	@echo "Building C++ Math Engine..."
	@g++ -O3 polyglot_core/cpp_engine/main.cpp -o bin/cpp-engine

# 4. Zig System Validator
build-zig:
	@echo "Building Zig System Validator..."
	@zig build-exe polyglot_core/zig_validator/main.zig -femit-bin=bin/zig-validator

# 5. Java Enterprise Bridge
build-java:
	@echo "Building Java Enterprise Bridge..."
	@javac polyglot_core/java_bridge/src/com/looseai/JavaBridge.java -d polyglot_core/java_bridge/bin
	@echo "Main-Class: com.looseai.JavaBridge" > polyglot_core/java_bridge/manifest.txt
	@jar cfm bin/java-bridge.jar polyglot_core/java_bridge/manifest.txt -C polyglot_core/java_bridge/bin .

clean:
	@echo "Cleaning binaries..."
	@rm -rf bin/*
	@rm -rf polyglot_core/java_bridge/bin/*
	@rm -f polyglot_core/java_bridge/manifest.txt

test:
	@echo "Running Unified Test Suite..."
	@python tests/test_core.py
	@go test ./polyglot_core/go_health_checker/...
	@cd polyglot_core/rust_secure_compute && cargo test
