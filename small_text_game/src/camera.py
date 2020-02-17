from small_text_game.src.options import SMOG


class Camera:
    def show(self, map, user, smog_radius):
        width, height = map.size()
        map_with_smog = self.apply_smog(map, user.position, smog_radius)
        print('-' * width)
        for y in range(height):
            print(''.join(map_with_smog[y]))
        print('-' * width)

    def apply_smog(self, map, position, radius):
        map_with_smog = []
        width, height = map.size()
        for y in range(0, height):
            map_with_smog.append(map.row(y).copy())
            for x in range(0, width):
                if x < position[0] - radius or x > position[0] + radius:
                    map_with_smog[y][x] = SMOG
                elif y < position[1] - radius or y > position[1] + radius:
                    map_with_smog[y][x] = SMOG
        return map_with_smog