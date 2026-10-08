# Mutant mixes C with a nasm source, which PwnableHarness's compile rules don't
# handle, so it's built with explicit rules (mirroring this folder's Makefile).
# Non-PIE like the original 2017 build: encrypt.asm uses absolute data addresses.
MUTANT_BUILD := $(BUILD_DIR)

$(MUTANT_BUILD)/encrypt.asm.o: $(DIR)/encrypt.asm
	$(_V)echo 'Assembling $@'
	$(_v)mkdir -p $(@D) && nasm -f elf64 -o $@ $<

$(MUTANT_BUILD)/mutant: $(DIR)/main.c $(MUTANT_BUILD)/encrypt.asm.o
	$(_V)echo 'Linking $@'
	$(_v)gcc -no-pie -o $@.raw $^ && strip -o $@ $@.raw

PUBLISH_BUILD := mutant
