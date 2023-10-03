import os
import pyvista as pv
import numpy as np

# 输入和输出目录
input_dir = "."
output_dir = "./output"

for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file== 'resistivity.vtk':
            # 拼接完整的文件路径
            vtk_file = file_path = os.path.join(root, file)
            # 在这里执行您的操作，例如打印文件路径
            #print(file_path)
            mesh = pv.read(vtk_file)

            # 获取单元格中心点
            centers = mesh.cell_centers()

            # 计算每个单元格中心点的坐标
            x_coordinates = centers.points[:, 0]
            y_coordinates = centers.points[:, 1]

            # 获取矢量数据
            cell_data = mesh.cell_data
            if "Resistivity" not in cell_data.keys():
                print(f"'Resistivity' not found in {vtk_file}")
                continue
            resistivity_array = cell_data["Resistivity"]

            # 以三列的形式组合数据：平均x， 平均y，Resistivity/Ohmm
            data = np.column_stack((x_coordinates, y_coordinates, resistivity_array))

            # 生成输出文件名
            subdir_name = os.path.basename(file)
            output_file = os.path.join(output_dir, f"{subdir_name}.txt")

            # 保存数据到txt文件
            np.savetxt(output_file, data, fmt="%f", delimiter="\t")
        else:
            print(f"'resistivity.vtk' not found in {file}")


            
            
