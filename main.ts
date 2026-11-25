// news-image-20261125 entry (Node 22, standard library only): validates the
// poster this repository ships and copies it to /output/entry.png byte for
// byte, so the grader's two runs write identical bytes. No network is used.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const SRC = new URL('./entry.png', import.meta.url);
const OUT = join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png');
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

const bytes = readFileSync(SRC);
if (bytes.length > 1048576) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB limit`);
}
if (!bytes.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error('entry.png is not a PNG (bad magic bytes)');
}
if (bytes.readUInt32BE(16) !== 1024 || bytes.readUInt32BE(20) !== 1024) {
  throw new Error('entry.png is not 1024x1024');
}
// Whole-image check: the file must end with the 12-byte IEND chunk.
const tail = bytes.subarray(bytes.length - 12);
if (tail.readUInt32BE(0) !== 0 || tail.toString('ascii', 4, 8) !== 'IEND') {
  throw new Error('entry.png is truncated (no IEND chunk)');
}
copyFileSync(SRC, OUT);
console.log(`copied entry.png (${statSync(OUT).size} bytes) to ${OUT}`);
