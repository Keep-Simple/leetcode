import fs from 'fs/promises'
import {
    getExampleFilesDir,
    getTestFilesDir,
    runSynonymsTask,
} from './synonyms'

describe.each(['example', 'example_big', 'test'])(
    'verify that %s.out is correct',
    (fileName: string) => {
        test('test ' + fileName, async () => {
            const inputFileName = fileName + '.in'
            const outputFileName = fileName + '.out'
            await runSynonymsTask(inputFileName, outputFileName)

            const expectedOutput = await fs.readFile(
                getExampleFilesDir(outputFileName)
            )
            const realOutput = await fs.readFile(
                getTestFilesDir(outputFileName)
            )

            expect(expectedOutput.compare(realOutput)).toBe(0)
        })
    }
)

afterAll(async () => {
    // empty test_files dir
    const files = await fs.readdir(getTestFilesDir())
    files.forEach((file) => fs.unlink(getTestFilesDir(file)))
})
